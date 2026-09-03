# Day 4 - AI Data Analyst: Text-to-SQL

## Project Overview

This project demonstrates how an LLM can act as an AI Data Analyst by converting natural language questions into SQL queries, executing those queries against a database, and explaining the results in simple business language.

The complete workflow is:

User Question → LLM → SQL Query → SQLite Database → Query Result → LLM → Business Explanation

## Example

User Question:

Which region generated the most revenue?

The LLM generates:

SELECT region, SUM(revenue) AS total_revenue
FROM sales
GROUP BY region
ORDER BY total_revenue DESC
LIMIT 1;

The SQL query is executed against the sales database, and the result is then passed back to the LLM for a business-friendly explanation.

## Database

The project uses SQLite and contains a `sales` table with 100 sample sales records.

### Sales Table

| Column        | Data Type |
| ------------- | --------- |
| order_id      | INTEGER   |
| order_date    | DATE      |
| customer_name | TEXT      |
| product       | TEXT      |
| region        | TEXT      |
| quantity      | INTEGER   |
| revenue       | REAL      |

## Features

* Natural language to SQL generation
* LLM-powered SQL generation using OpenRouter
* SQLite database integration
* Automatic SQL execution
* Query result retrieval
* Business-friendly result explanation
* Basic SQL security validation
* Only SELECT queries are allowed
* Blocks data-changing SQL operations

## Security

LLM-generated SQL should never be blindly executed in a real production environment.

This project includes a basic validation layer that:

* Allows only SELECT queries
* Blocks INSERT
* Blocks UPDATE
* Blocks DELETE
* Blocks DROP
* Blocks ALTER
* Blocks CREATE
* Blocks REPLACE
* Blocks TRUNCATE

For a production system, stronger SQL parsing, read-only database permissions, query timeouts, and additional validation should be implemented.

## Example Questions

The application was tested with questions such as:

* Which region generated the most revenue?
* Which product generated the most revenue?
* What is the total revenue generated?
* Which region sold the most quantity?
* How much revenue did each region generate?

## Technologies Used

* Python
* OpenRouter API
* OpenAI Python SDK
* SQLite
* python-dotenv
* LLM / Generative AI
* Text-to-SQL

## Project Structure

day4_text_to_sql/

├── generate_data.py
├── sql_generator.py
├── sales.db
└── README.txt

## How to Run

### 1. Generate the database

Run:

python generate_data.py

This creates the `sales.db` SQLite database containing sample sales data.

### 2. Configure the API key

The project uses an `.env` file in the main project folder.

Example:

OPENROUTER_API_KEY=your_api_key_here

Do not commit the actual API key to GitHub.

### 3. Run the AI Data Analyst

Run:

python sql_generator.py

Enter a natural language question when prompted.

Example:

Which region generated the most revenue?

The application will:

1. Generate SQL using the LLM.
2. Validate the SQL.
3. Execute the query against SQLite.
4. Display the query result.
5. Ask the LLM to explain the result in business language.

## Learning Objectives

This project demonstrates practical concepts in:

* Large Language Models
* Prompt Engineering
* Text-to-SQL
* Database interaction with Python
* LLM + SQL integration
* Basic AI application security
* Business-oriented AI responses

## Future Improvements

Possible future improvements include:

* Support for SQL Server and PostgreSQL
* Better SQL validation using a SQL parser
* Read-only database users
* Conversation history
* Follow-up questions
* Automatic charts and visualizations
* Multiple database/table support
* Improved error handling
* Query performance optimization
* Streamlit web interface

## Author

Rajat Shakya

LLM & AI Learning Journey - Day 4
