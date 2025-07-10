import json
from openai_agent import parse_lead_message
from email_utils import send_followup_email
from crm_utils import add_lead_to_crm

def main():
    print("=== Sales Follow-up Agent ===")
    user_input = input("Paste new lead message: ")

    # Parse using GPT
    lead_info = parse_lead_message(user_input)

    if lead_info:
        print(f"Parsed Lead Info: {lead_info}")

        # Send email
        send_followup_email(
            lead_info['name'],
            lead_info['email'],
            lead_info['interest']
        )

        # Update CRM
        add_lead_to_crm(**lead_info)

        print(f"✅ Follow-up email sent and CRM updated for {lead_info['name']}")
    else:
        print("❌ Could not parse the lead message.")

if __name__ == "__main__":
    main()
