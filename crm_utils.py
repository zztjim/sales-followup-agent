import json
import os

def add_lead_to_crm(name, email, company, interest, crm_file='crm.json'):
    if os.path.exists(crm_file):
        with open(crm_file, 'r') as file:
            crm_data = json.load(file)
    else:
        crm_data = []

    crm_data.append({
        "name": name,
        "email": email,
        "company": company,
        "interest": interest
    })

    with open(crm_file, 'w') as file:
        json.dump(crm_data, file, indent=4)

    print(f"💾 Lead added to CRM: {name} - {email}")
