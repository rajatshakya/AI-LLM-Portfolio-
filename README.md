# LLM-Powered Customer Support Ticket Classifier

An LLM-powered customer support ticket classification system that automatically categorizes customer queries into predefined support categories such as **Login, Payment, Technical, and Other**.

The project demonstrates how Large Language Models (LLMs) can be integrated into a Python-based workflow to automate repetitive customer support operations and produce structured classification results.

## 🚀 Project Overview

Customer support teams receive a large volume of tickets every day. Manually reviewing and categorizing these tickets can be time-consuming and inconsistent.

This project automates the initial ticket-triage process:

**Customer Ticket → LLM → Category → CSV Output**

The system sends each support ticket to an LLM through the OpenRouter API, receives the predicted category, and stores the results in a CSV file for further processing or analysis.

## 🎯 Business Objective

The primary objective is to reduce manual effort involved in ticket categorization and provide a scalable foundation for automated support-ticket routing.

Potential business applications include:

* Automated ticket triage
* Support queue routing
* Priority-based workflow automation
* Customer service analytics
* Reducing repetitive manual classification
* Integration with CRM or help-desk platforms

## 🛠️ Technologies Used

* **Python 3.13**
* **OpenRouter API**
* **LLM – Ling 3.0 Flash**
* Python `openai` package
* `python-dotenv`
* Python `csv` module
* Git & GitHub

## ⚙️ How It Works

1. Customer support tickets are provided as input.
2. Python iterates through each ticket using a `for` loop.
3. Each ticket is sent to the LLM through the OpenRouter API.
4. The LLM classifies the ticket into a predefined category.
5. The classification result is stored in Python.
6. All results are exported to a CSV file.

### Workflow

```text
             Customer Support Tickets
                       │
                       ▼
                  Python Script
                       │
                       ▼
                  For Loop
                       │
                       ▼
                OpenRouter API
                       │
                       ▼
                     LLM
                       │
                       ▼
              Ticket Classification
                       │
                       ▼
              Structured Results
                       │
                       ▼
             classified_tickets.csv
```

## 📂 Project Structure

```text
LLM-Ticket-Classifier/
│
├── ticket_classifier.py       # Main Python application
├── classified_tickets.csv     # Classified ticket results
├── .gitignore                 # Prevents sensitive files from being committed
└── README.md                  # Project documentation
```

> **Note:** The `.env` file containing the API key is intentionally excluded from the repository for security reasons.

## 📊 Example

### Input

```text
Customer is unable to login
```

### Output

```text
Login
```

Another example:

```text
My credit card was charged twice
```

Output:

```text
Payment
```

The system can process multiple tickets automatically rather than requiring individual manual classification.

## 🔐 Environment Configuration

Create a `.env` file in the project directory:

```text
OPENROUTER_API_KEY=your_api_key_here
```

The API key is loaded securely using `python-dotenv` and is not hard-coded into the Python application.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/rajatshakya/LLM-Ticket-Classifier.git
cd LLM-Ticket-Classifier
```

### 2. Install dependencies

```bash
pip install openai python-dotenv
```

### 3. Configure your API key

Create a `.env` file:

```text
OPENROUTER_API_KEY=your_api_key_here
```

### 4. Run the application

```bash
python ticket_classifier.py
```

The classified results will be saved to:

```text
classified_tickets.csv
```

## 💡 Key Learning Outcomes

This project demonstrates practical implementation of:

* LLM API integration
* Prompt-based text classification
* Environment variable management
* Python loops and data structures
* Processing multiple inputs through an LLM
* Structured result collection
* CSV generation
* Basic Git version control
* GitHub project management

## 🔮 Future Enhancements

The current implementation provides a foundation that can be extended into a production-oriented ticket automation system.

Potential improvements include:

* Add more support categories
* Return structured JSON responses
* Add ticket priority classification
* Add sentiment analysis
* Detect customer intent
* Process large CSV datasets automatically
* Add confidence scores
* Integrate with Zendesk, Jira, or other ticketing systems
* Automatically route tickets to the appropriate support team
* Build a web interface for uploading ticket files
* Add logging and error handling
* Implement batch processing for large ticket volumes

## 📌 Project Status

**Version:** 1.0
**Status:** Completed – Initial LLM Classification Pipeline

This project is part of a practical learning journey focused on **LLM application development, AI automation, and real-world business use cases**.
