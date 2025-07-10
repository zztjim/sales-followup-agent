import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_lead_message(user_input):
    functions = [
        {
            "name": "process_new_lead",
            "description": "Extract lead info and take follow-up actions",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "company": {"type": "string"},
                    "interest": {"type": "string"}
                },
                "required": ["name", "email", "company", "interest"]
            }
        }
    ]

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_input}],
        functions=functions,
        function_call="auto"
    )

    try:
        arguments = response["choices"][0]["message"]["function_call"]["arguments"]
        return json.loads(arguments)
    except Exception as e:
        print("Error parsing GPT function response:", e)
        return None
