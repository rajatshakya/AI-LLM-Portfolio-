DAY 3 – RAG CHATBOT PROJECT

Project: Policy Document RAG Chatbot

## OVERVIEW

This project demonstrates a basic Retrieval-Augmented Generation (RAG) chatbot using Python.

The chatbot allows users to ask questions about company policy documents. Instead of sending the complete documents to the LLM for every question, the system first searches the relevant information from the stored documents and then uses that information to generate an answer.

The project uses:

* Python
* OpenAI API
* ChromaDB
* Embeddings
* Retrieval-Augmented Generation (RAG)

## PROJECT STRUCTURE

day3_rag/
│
├── documents/
│   ├── insurance_policy.txt
│   ├── leave_policy.txt
│   ├── travel_policy.txt
│   ├── wfh_policy.txt
│   └── leave_ policy.pdf
│
├── chroma_db/
│   └── Local vector database
│
├── rag_chatbot.py
├── .gitignore
└── README.txt

## HOW RAG WORKS

The project follows these main steps:

1. DOCUMENT LOADING
   Policy documents are loaded from the documents folder.

2. TEXT PROCESSING
   The document content is read and prepared for processing.

3. EMBEDDINGS
   The text is converted into numerical vector representations called embeddings.

4. VECTOR DATABASE
   The embeddings are stored in ChromaDB.

5. USER QUESTION
   The user enters a question about a policy.

6. RETRIEVAL
   The system searches ChromaDB for the most relevant pieces of information.

7. GENERATION
   The retrieved information is provided as context to the LLM.

8. FINAL ANSWER
   The LLM generates an answer based on the retrieved policy information.

## EXAMPLE QUESTIONS

You can ask questions such as:

* How many days of leave can an employee take?
* What is the work from home policy?
* What is the travel reimbursement policy?
* What are the insurance benefits?
* Can I work from home?
* What is the eligibility for leave?
* How does the company handle business travel?

## WHY RAG?

A normal LLM may not know about private or company-specific documents.

RAG allows the application to provide relevant information from external documents to the LLM before generating the response.

This helps the chatbot:

* Answer questions using specific documents
* Work with private or custom knowledge
* Reduce irrelevant responses
* Keep the knowledge base separate from the LLM
* Update information by updating the documents

## TECHNOLOGIES USED

Python
OpenAI API
ChromaDB
Vector Embeddings
RAG
Text Documents
PDF Documents

## CHROMADB

ChromaDB is used as the local vector database for storing document embeddings and retrieving relevant information.

The chroma_db folder is generated locally by the application and is ignored by Git using .gitignore.

It does not need to be uploaded to GitHub because the database can be recreated from the source documents.

## HOW TO RUN

1. Make sure Python is installed.

2. Install the required Python packages.

3. Configure the OpenAI API key in the environment variables or .env file.

4. Navigate to the project folder.

5. Run:

   python rag_chatbot.py

6. Enter your questions when prompted.

## LEARNING OBJECTIVES

This project was created to understand the fundamentals of RAG systems.

Key concepts covered:

* What is RAG?
* Document ingestion
* Text processing
* Embeddings
* Vector databases
* Similarity search
* Context retrieval
* LLM response generation
* Connecting an LLM with external knowledge

## FUTURE IMPROVEMENTS

Possible improvements include:

* Better document chunking
* Metadata filtering
* Support for more PDF documents
* Source citations in chatbot responses
* Conversation memory
* Improved prompt engineering
* Web-based chatbot interface
* Streamlit interface
* Multiple knowledge bases
* Hybrid search

## PROJECT GOAL

The goal of this project is to build a simple end-to-end RAG application and understand how modern AI applications connect documents, vector databases, embeddings, retrieval, and Large Language Models.
