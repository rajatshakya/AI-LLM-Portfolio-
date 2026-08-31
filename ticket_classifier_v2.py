from openai import OpenAI
from dotenv import load_dotenv
import os
import csv
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

results = []

print("Ticket classifier project started")

tickets = [
    "Customer is unable to login",
    "my credit card was charged twice",
    "application crashes when I open the app",
    "I want to change my registered email address",
    "I cannot reset my password",
    "i am still waiting for my refund of room cancellation",
    "why i recevie spam email from your company",
    "unable to send the campaign emails through your app"
]

for ticket in tickets:

    print("\nTicket:", ticket)

    try:
        response = client.chat.completions.create(
            model="inclusionai/ling-3.0-flash-fin:free",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": """
You are a customer support ticket classifier.

Classify each ticket into exactly one of these categories:
Login, Payment, Technical, or Other.

Also determine:
- Priority: High, Medium, or Low
- Sentiment: Positive, Neutral, or Negative
- Summary: A short summary of the customer's issue

Return ONLY valid JSON.
Do not use markdown.
Do not use ```json.
Do not provide any explanation.

Use exactly this JSON format:
{
    "category": "Login",
    "priority": "High",
    "sentiment": "Negative",
    "summary": "Customer is unable to login"
}
"""
                },
                {
                    "role": "user",
                    "content": f"Ticket: {ticket}"
                }
            ]
        )

        raw_response = response.choices[0].message.content

        print("Raw LLM Response:", raw_response)

        clean_response = (
            raw_response
            .replace("```json", "")
            .replace("```", "")
            .strip()
        )

        result = json.loads(clean_response)

        category = result["category"]
        priority = result["priority"]
        sentiment = result["sentiment"]
        summary = result["summary"]

        print("Category:", category)
        print("Priority:", priority)
        print("Sentiment:", sentiment)
        print("Summary:", summary)

        if response.usage:
            input_tokens = response.usage.prompt_tokens
            output_tokens = response.usage.completion_tokens
            total_tokens = response.usage.total_tokens
        else:
            input_tokens = ""
            output_tokens = ""
            total_tokens = ""

        results.append([
            ticket,
            category,
            priority,
            sentiment,
            summary,
            input_tokens,
            output_tokens,
            total_tokens
        ])

    except json.JSONDecodeError:
        print("Error: LLM returned invalid JSON.")
        results.append([
            ticket,
            "ERROR",
            "",
            "",
            "Invalid JSON response",
            "",
            "",
            ""
        ])

    except Exception as e:
        print("API or application error:", e)
        results.append([
            ticket,
            "ERROR",
            "",
            "",
            str(e),
            "",
            "",
            ""
        ])


with open(
    "classified_tickets_v2.csv",
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Ticket",
        "Category",
        "Priority",
        "Sentiment",
        "Summary",
        "Input Tokens",
        "Output Tokens",
        "Total Tokens"
    ])

    writer.writerows(results)


print("\nCSV file created successfully!")