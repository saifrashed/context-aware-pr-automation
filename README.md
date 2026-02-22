# Context Aware PR Automation
This project creates an automated GitHub Actions workflow that detects new Pull Requests and uses a Python script to aggregate code diffs, commit history, and linked project data. It then sends this context to the OpenAI API to generate and publish a structured, professional PR description, saving developers time and enforcing consistent documentation.

## Setup
1. Generate OpenAI API key
- Go to platform.openai.com/api-keys.
- Log in (or sign up).
- Click "Create new secret key".
- Name it something like "GitHub PR Action".
- Copy the key immediately (starts with sk-...). You won't be able to see it again.

2. Generate Github Personal Access Token
- Go to Settings (Profile) -> Developer Settings -> Personal Access Tokens -> Tokens (Classic).
- Generate New Token (Classic).
- Scopes: Check repo, read:org, and crucially read:project (or project).
- Copy the token (ghp_...).

3. Add to Secrets:
- Go to Repo Settings -> Secrets and variables -> Actions.
- Add New Repository Secret: PAT_KEY & OPENAI_API_KEY.


## Run example scripts

1. Run the app:
```
python main.py
```
2. Run the tests:
```
python test.py
```

3. Expected Output for test.py:
```
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK
```