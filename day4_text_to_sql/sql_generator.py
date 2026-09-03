import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# Load .env from the parent project folder
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

# Create OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Database schema
schema = """
Table: sales

Columns:
- order_id: INTEGER
- order_date: DATE
- customer_name: TEXT
- product: TEXT
- region: TEXT
- quantity: INTEGER
- revenue: REAL
"""

question = input("Ask a question about the sales data: ")

prompt = f"""
You are an expert SQL analyst.

Convert the user's natural language question into a SQLite SQL query.

Database schema:
{schema}

Rules:
1. Generate ONLY SQL.
2. Use only the sales table.
3. Only generate SELECT queries.
4. Do not use INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, or other data-changing operations.
5. Use SQLite-compatible SQL.

User question:
{question}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0
)

sql_query = response.choices[0].message.content.strip()

# Remove markdown code fences if the LLM adds them
sql_query = sql_query.replace("```sql", "").replace("```", "").strip()

print("\nGenerated SQL:")
print(sql_query)

import sqlite3

db_path = Path(__file__).resolve().parent / "sales.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Basic SQL security validation
sql_upper = sql_query.upper().strip()

if not sql_upper.startswith("SELECT"):
    print("\nError: Only SELECT queries are allowed.")
    conn.close()
    exit()

blocked_keywords = [
    "INSERT",
    "UPDATE",
    "DELETE",
    "DROP",
    "ALTER",
    "CREATE",
    "REPLACE",
    "TRUNCATE"
]

for keyword in blocked_keywords:
    if keyword in sql_upper:
        print(f"\nError: {keyword} operation is not allowed.")
        conn.close()
        exit()

cursor.execute(sql_query)

result = cursor.fetchall()

print("\nQuery Result:")
print(result)

conn.close()

explanation_prompt = f"""
You are a business data analyst.

The user asked:
{question}

The SQL query returned this result:
{result}

Explain the result in simple business language.
Important:
- Revenue values are in Indian Rupees (INR).
- Use ₹ when mentioning revenue.
- Do not convert the amount to dollars or any other currency.
- Mention the region and exact revenue clearly.
- Do not mention SQL or technical details.
"""

explanation_response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {"role": "user", "content": explanation_prompt}
    ],
    temperature=0
)

explanation = explanation_response.choices[0].message.content.strip()

print("\nBusiness Explanation:")
print(explanation)