import os
import subprocess
import json
import requests
import sys

# Configuration
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
REPO_OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER")
REPO_NAME = os.environ.get("GITHUB_REPOSITORY").split("/")[-1]
PR_NUMBER = os.environ.get("PR_NUMBER")
TEMPLATE_PATH = ".github/templates/pr-report.md"

if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY is missing.")
    sys.exit(1)

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return ""

def get_pr_diff():
    # Limit diff to 3000 chars to save tokens and prevent errors
    diff = run_command(f"git diff origin/main...HEAD")
    if len(diff) > 3000:
        return diff[:3000] + "\n...[Diff truncated due to length]..."
    return diff

def get_commit_log():
    return run_command("git log --pretty=format:'- %s (%an)' origin/main..HEAD")

def get_linked_issues():
    # Fetch issues linked via "Closes #123" or manually linked in UI
    try:
        # We need the body to check for "Closes #" text AND the API for linked issues
        cmd = f"gh pr view {PR_NUMBER} --json title,body,closingIssuesItems"
        data = run_command(cmd)
        json_data = json.loads(data)
        
        issues = json_data.get("closingIssuesItems", [])
        
        if not issues:
            return "No linked issues found."
            
        return "\n".join([f"- **#{i['number']}**: {i['title']}" for i in issues])
    except Exception as e:
        return f"Could not fetch linked issues: {str(e)}"

def generate_description():
    # 1. Gather Context
    diff = get_pr_diff()
    commits = get_commit_log()
    issues = get_linked_issues()
    
    with open(TEMPLATE_PATH, "r") as f:
        template = f.read()

    # 2. Construct Prompt
    system_prompt = "You are a helpful assistant acting as a Senior Developer. Your job is to fill out a Pull Request template based on code changes."
    
    user_prompt = f"""
    Please fill out the following Markdown template with the provided context.
    
    TEMPLATE:
    {template}
    
    CONTEXT:
    1. Linked Issues:
    {issues}
    
    2. Commit History:
    {commits}
    
    3. Code Diff (Changes):
    {diff}
    
    INSTRUCTIONS:
    - Keep the summary concise.
    - Use the provided template structure exactly.
    - Do not invent information not present in the diff or commits.
    """

    # 3. Call OpenAI
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo", # Or "gpt-4" if you have access and budget
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.5
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    
    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        print(content) # Print to stdout so bash can capture it
    else:
        print(f"Error calling OpenAI: {response.text}")
        sys.exit(1)

if __name__ == "__main__":
    generate_description()