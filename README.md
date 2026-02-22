# Context Aware PR Automation


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
