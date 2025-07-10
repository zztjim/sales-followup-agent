# sales-followup-agent

## Overview
This project demonstrates an AI-powered agent that automates sales lead follow-up. The agent:
- Parses new lead messages using OpenAI GPT function calling.
- Sends an automated thank-you email via SMTP.
- Updates a mock CRM stored in a local JSON file.

## Actions Performed
1. Parses natural language input (lead message).
2. Extracts lead name, email, company, and product interest.
3. Sends a follow-up email.
4. Updates CRM data.

## Architecture
```
[User Message]
     ↓
[OpenAI GPT Function Calling]
     ↓
[SMTP Server (Gmail)]
     ↓
[CRM JSON Storage]
```

## Example User Input
```
John Doe from Acme Corp is interested in our Pro plan. His email is john@acme.com.
```

## Example Logs
```
Parsed Lead Info: {'name': 'John Doe', 'email': 'john@acme.com', 'company': 'Acme Corp', 'interest': 'Pro plan'}
📧 Email sent to john@acme.com
💾 Lead added to CRM: John Doe - john@acme.com
✅ Follow-up email sent and CRM updated for John Doe
```

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set OpenAI API Key
```bash
export OPENAI_API_KEY=sk-...
```

### 3. Configure Email Credentials
Edit `email_utils.py` with your Gmail address and an app password (recommended).

### 4. Run the Agent
```bash
python app.py
```

## CRM Data
CRM leads are stored in `crm.json` as a list of dictionaries.
