# LLM Ticket Classifier

A Python-based customer support ticket classification application that uses an LLM through the OpenRouter API to automatically analyze and categorize customer support tickets.

The project demonstrates how a Python application can communicate with an LLM, provide structured instructions, receive structured JSON output, handle errors, track token usage, and export results to CSV.

## 🚀 Project Overview

Customer support teams receive a large number of tickets every day. Manually categorizing these tickets can be time-consuming.

This project automates the initial classification process using an LLM.

### Input

Example customer ticket:

> "My credit card was charged twice."

### Output

```json
{
  "category": "Payment",
  "priority": "High",
  "sentiment": "Negative",
  "summary": "Customer reports their credit card was charged twice"
}
```

---

# 🛠️ Technologies Used

* Python
* OpenRouter API
* OpenAI Python SDK
* JSON
* CSV
* python-dotenv
* Git & GitHub

---

# 📌 Version 1 — Basic Ticket Classifier

The first version focuses on the fundamentals of integrating Python with an LLM.

### Features

* Connects Python application to an LLM API
* Sends customer support tickets to the LLM
* Classifies tickets into:

  * Login
  * Payment
  * Technical
  * Other
* Processes multiple tickets using a Python loop
* Exports classification results to CSV

### Flow

```text
Customer Ticket
      ↓
Python Application
      ↓
LLM API
      ↓
Classification
      ↓
CSV File
```

### Files

`ticket_classifier.py`
Basic LLM-powered ticket classification application.

`classified_tickets.csv`
CSV containing the classification results.

---

# 📈 Version 2 — Structured LLM Ticket Classifier

Version 2 improves the application by introducing structured LLM responses and basic production-oriented practices.

### Features

#### 1. System & User Prompts

A system prompt defines the role and rules for the LLM, while the user prompt contains the actual customer ticket.

#### 2. Structured JSON Output

The LLM is instructed to return structured JSON containing:

* Category
* Priority
* Sentiment
* Summary

#### 3. JSON Parsing

The application uses Python's `json` module to convert the LLM's JSON response into a Python dictionary.

#### 4. Error Handling

The application handles:

* Invalid JSON responses
* API/application errors

A failed ticket does not stop the processing of the remaining tickets.

#### 5. Token Usage Tracking

The application captures:

* Input tokens
* Output tokens
* Total tokens

This can be used for monitoring and future API cost calculations.

#### 6. CSV Export

The final structured results are exported to CSV for further analysis or reporting.

### Version 2 Flow

```text
Customer Ticket
      ↓
Python
      ↓
System Prompt + User Prompt
      ↓
LLM API
      ↓
Structured JSON
      ↓
JSON Parsing
      ↓
Error Handling
      ↓
Token Usage
      ↓
CSV Output
```

### Files

`ticket_classifier_v2.py`
Upgraded ticket classification application.

`classified_tickets_v2.csv`
Structured classification results including category, priority, sentiment, summary, and token usage.

---

# 💡 Example Categories

| Ticket                          | Category  | Priority | Sentiment |
| ------------------------------- | --------- | -------- | --------- |
| Customer is unable to login     | Login     | High     | Negative  |
| Credit card was charged twice   | Payment   | High     | Negative  |
| Application crashes             | Technical | High     | Negative  |
| Change registered email address | Other     | Medium   | Neutral   |

---

# 🔐 Security

API credentials are stored using environment variables rather than hard-coded in the Python source code.

The `.env` file is excluded from Git using `.gitignore`.

**Never commit API keys or other sensitive credentials to a public repository.**

---

# 🎯 Skills Demonstrated

This project demonstrates practical understanding of:

* LLM API integration
* Prompt engineering
* System vs. user prompts
* Structured LLM output
* JSON parsing
* Python exception handling
* Environment variables
* Token usage tracking
* CSV processing
* Git & GitHub
* Basic LLM application architecture

---

# 🔮 Possible Future Improvements

The project can be extended with:

* More support ticket categories
* Confidence scores
* Batch processing
* Database storage
* REST API using FastAPI
* Web interface
* Logging and monitoring
* Retry mechanisms for API failures
* Automated evaluation of classification accuracy
* Vector database and semantic search

---

# 👨‍💻 Author

**Rajat Shakya**

This project is part of my hands-on learning journey in **LLMs, Generative AI, and AI application development**.
