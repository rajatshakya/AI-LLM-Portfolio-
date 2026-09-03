from openai import OpenAI
from dotenv import load_dotenv
import os
import csv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

results = []

print ("Ticket classifier project started")
tickets = ["Customer is unable to login",
          "my credit card was charged twice",
          "application crashes when I open the app",
          "I want to change my registered email address",
          "I cannot reset my password",
          "i am still waiting for my refund of room cancellation",
          "why i recevie spam email from your company",
          "unable to send the campaign emails through your app"]

for ticket in tickets:
    print("Ticket:", ticket)

    response = client.chat.completions.create(
        model="inclusionai/ling-3.0-flash-fin:free",
        messages=[
            {
                "role": "user",
                "content": f"Classify this support ticket into one category: Login, Payment, Technical, or Other.\n\nTicket: {ticket}"
            }
        ]
    )

    category = response.choices[0].message.content

    print("LLM Response:", category)

    results.append([ticket, category])

with open("classified_tickets.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Ticket", "Category"])
    writer.writerows(results)

print("CSV file created successfully!")

