import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI


# Load API key from root .env
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


# Simulated ticket creation tool
def create_ticket(category, priority, summary):
    ticket_id = "TICKET-1001"

    print("\n--- Support Ticket Created ---")
    print("Ticket ID:", ticket_id)
    print("Category:", category)
    print("Priority:", priority)
    print("Summary:", summary)

    return {
        "ticket_id": ticket_id,
        "status": "Created",
        "category": category,
        "priority": priority,
        "summary": summary
    }


# Get customer message
customer_message = input("Customer message: ")


# AI agent instructions
system_prompt = """
You are an AI customer support agent.

Analyze the customer's message.

If the customer has a problem that requires support,
use the create_ticket tool.

Choose the appropriate category and priority.

Allowed categories:
Billing, Technical, Account, Booking, Other

Allowed priorities:
Low, Medium, High

Create a ticket for genuine customer problems.

Do not create a ticket for:
- Greetings
- Thank-you messages
- General casual conversation

After the ticket is created, the system will generate
a suggested response for the customer.
"""


# Tool available to the AI agent
tools = [
    {
        "type": "function",
        "function": {
            "name": "create_ticket",
            "description": "Create a customer support ticket for a genuine customer issue.",
            "parameters": {
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "enum": [
                            "Billing",
                            "Technical",
                            "Account",
                            "Booking",
                            "Other"
                        ]
                    },
                    "priority": {
                        "type": "string",
                        "enum": [
                            "Low",
                            "Medium",
                            "High"
                        ]
                    },
                    "summary": {
                        "type": "string"
                    }
                },
                "required": [
                    "category",
                    "priority",
                    "summary"
                ]
            }
        }
    }
]


# Ask the AI to analyze the customer message
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": customer_message
        }
    ],
    tools=tools,
    tool_choice="auto",
    temperature=0
)


message = response.choices[0].message


# Check if the AI decided to use a tool
if message.tool_calls:

    for tool_call in message.tool_calls:

        if tool_call.function.name == "create_ticket":

            arguments = json.loads(tool_call.function.arguments)

            category = arguments["category"]
            priority = arguments["priority"]
            summary = arguments["summary"]


            # Guardrails
            allowed_categories = [
                "Billing",
                "Technical",
                "Account",
                "Booking",
                "Other"
            ]

            allowed_priorities = [
                "Low",
                "Medium",
                "High"
            ]

            if category not in allowed_categories:
                print("\nError: Invalid category.")
                exit()

            if priority not in allowed_priorities:
                print("\nError: Invalid priority.")
                exit()


            # Execute the tool
            ticket = create_ticket(
                category,
                priority,
                summary
            )


            # Generate suggested response
            response_prompt = f"""
You are a professional customer support representative.

Write a short and polite response to the customer.

Customer message:
{customer_message}

Ticket information:
Ticket ID: {ticket["ticket_id"]}
Category: {ticket["category"]}
Priority: {ticket["priority"]}
Summary: {ticket["summary"]}

Tell the customer that their issue has been registered
and provide the ticket ID.

Do not mention AI, LLM, tools, or internal systems.
"""


            response_message = client.chat.completions.create(
                model="openai/gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": response_prompt
                    }
                ],
                temperature=0.3
            )


            suggested_response = (
                response_message
                .choices[0]
                .message
                .content
                .strip()
            )


            # Human-in-the-loop
            print("\n--- Suggested Customer Response ---")
            print(suggested_response)

            approval = input(
                "\nSend this response? (yes/no): "
            ).strip().lower()

            if approval == "yes":
                print("\nResponse approved and sent! 📩")
            else:
                print("\nResponse was not sent. Human review required. 🧑‍💼")


else:

    print("\nAI Response:")
    print(message.content)