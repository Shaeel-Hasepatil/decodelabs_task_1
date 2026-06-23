# 🤖 RuleBot — Hybrid AI Chatbot

A hybrid chatbot built as part of the **DecodeLabs Internship - Project 1**.

RuleBot combines the speed of a traditional rule-based chatbot with the flexibility of a Large Language Model (LLM). Known user inputs are handled instantly through predefined responses, while unknown queries are forwarded to Groq's Llama model for intelligent responses.

---

## 🚀 Features

* Rule-based chatbot using Python dictionaries
* Instant response for predefined intents
* AI-powered fallback using Groq LLM
* Input sanitization and preprocessing
* Error handling for API failures
* Modular and easy-to-understand code structure
* Infinite chat loop with exit commands

---

## 🏗️ Project Architecture

```text
User Input
     │
     ▼
Input Sanitization
     │
     ▼
Rule Matching
     │
 ┌───┴───┐
 │ Match │
 └───┬───┘
     │
     ▼
Rule-Based Response

No Match
     │
     ▼
Groq LLM API
     │
     ▼
AI Generated Response
```

---

## 📂 Project Structure

```text
Project-1_AI_ChatBox/
│
├── modifiedMain.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Technologies Used

* Python 3
* Groq API
* Llama 3.3 70B Versatile Model
* python-dotenv

---

## 🔧 Installation

### Clone the Repository

```bash
git clone <repository-url>
cd Project-1_AI_ChatBox
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create a .env File

```env
GROQ_API_KEY=your_api_key_here
```

### Run the Chatbot

```bash
python modifiedMain.py
```

---

## 💬 Example Usage

```text
You: hello

[Rule Match ✅]
RuleBot: Hey there! I'm RuleBot. How can I help you today?
```

```text
You: What is the capital of France?

[No Rule Found → Asking Groq LLM... 🤖]
RuleBot: Paris is the capital of France.
```

---

## 🎯 Learning Outcomes

This project demonstrates:

* Dictionaries and key-value lookups
* Function-based program design
* Conditional logic
* API integration
* Environment variable management
* Hybrid AI architecture
* Error handling

---

## 👨‍💻 Author

Shaeel Hasepatil

DecodeLabs Internship — Project 1
