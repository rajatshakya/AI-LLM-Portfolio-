# Day 5 — AI Support Agent

## Project Overview

This project is a simple AI-powered customer support agent.

The agent can understand a customer's message, identify the type and priority of the issue, decide whether a support ticket is required, create a ticket using a tool, and generate a suggested response for the customer.

A human approval step is included before the response is sent.

## Architecture

```text
Customer Message
       ↓
      LLM
       ↓
Analyze Customer Issue
       ↓
Decide Whether Tool Is Required
       ↓
create_ticket()
       ↓
Support Ticket Created
       ↓
Generate Customer Response
       ↓
Human Approval
       ↓
Response Sent
```

## Example

### Customer Message

```text
I've been charged twice for my booking.
```

### AI Analysis

```text
Category: Billing
Priority: High
Sentiment: Negative
Product: Booking
```

### Tool Action

```text
Ticket ID: TICKET-1001
Category: Billing
Priority: High
```

The agent then generates a suggested response and asks for human approval before sending it.

## Key Concepts

### 1. Structured Output

The AI analyzes the customer message and produces structured information such as:

* Category
* Priority
* Sentiment
* Product
* Summary

### 2. Guardrails

The Python application validates the AI-generated information before performing an action.

For example, the category must be one of:

```text
Billing
Technical
Account
Booking
Other
```

### 3. Tool Calling

The AI has access to a `create_ticket` tool.

The AI decides when the tool should be used and provides the required arguments.

The current project uses a simulated Python function instead of a real Zendesk or Jira integration.

### 4. Human-in-the-Loop

The AI generates a customer response, but a human must approve it before it is considered sent.

This helps prevent incorrect or inappropriate automated responses.

## Technologies Used

* Python
* OpenAI Python SDK
* OpenRouter
* Python JSON
* python-dotenv
* LLM Tool Calling

## Project Structure

```text
day5_ai_support_agent/
│
├── support_agent.py
└── README.md
```

## How to Run

Make sure the `.env` file in the parent project folder contains:

```text
OPENROUTER_API_KEY=your_api_key
```

Run the project from the root folder:

```powershell
& "C:\Users\om\AppData\Local\Programs\Python\Python313\python.exe" ".\day5_ai_support_agent\support_agent.py"
```

Enter a customer message when prompted.

Example:

```text
The application crashes every time I try to login.
```

## Important Note

This is a learning and portfolio project.

The ticket creation functionality is simulated using a Python function. In a production environment, the same tool could be connected to systems such as Zendesk, Jira, or another ticketing platform through their APIs.

## Learning Outcomes

This project demonstrates how an LLM can move beyond simple question-answering and participate in an action-oriented workflow.

Key concepts learned:

* LLM-based classification
* Structured outputs
* JSON parsing
* Guardrails
* Function/Tool Calling
* Agent workflows
* Human-in-the-loop
* AI-generated customer responses

## Future Improvements

* Connect the ticket tool to Zendesk or Jira API
* Add authentication and user permissions
* Store tickets in a database
* Add multiple tools
* Add ticket assignment to support teams
* Add conversation history
* Build a Streamlit or web-based interface

## Author

Rajat Shakya

LLM & AI Learning Portfolio
