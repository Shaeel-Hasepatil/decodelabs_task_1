# ============================================================
"""
DecodeLabs Internship
Project 1: Hybrid AI Chatbot
  Rule-Based  +  Groq LLM Fallback
  Architecture: If rule matches → instant reply
                If no match    → Groq LLM handles it

Features:
1. Rule-based response system
2. Groq LLM fallback
3. Input sanitization
4. Error handling
5. Modular architecture

Author: Shaeel Hasepatil
"""
# ============================================================
from dotenv import load_dotenv
import os
from groq import Groq

# ── KNOWLEDGE BASE ───────────────────────────────────────────
responses = {
    "hello":       "Hey there! I'm RuleBot. How can I help you today?",
    "hi":          "Hi! Great to meet you. What's on your mind?",
    "hey":         "Hey! What can I do for you?",
    "bye":         "Goodbye! Have a great day!",
    "goodbye":     "See you later! Take care!",
    "how are you": "I'm just a bunch of if-else logic, but I'm doing great!",
    "who are you": "I'm RuleBot, a hybrid chatbot built for DecodeLabs Project 1.",
    "what can you do": "I can respond to rules instantly, and hand off unknown questions to an AI!",
    "help":        "Try saying: hello, how are you, who are you, what is ai, joke, or anything else!",
    "what is ai":  "AI stands for Artificial Intelligence — teaching machines to simulate human decision-making.",
    "what is ml":  "Machine Learning is a subset of AI where systems learn from data instead of explicit rules.",
    "what is python": "Python is a beginner-friendly programming language — great for AI projects!",
    "joke":        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
}

# ── GROQ LLM SETUP ──────────────────────────────────────────
load_dotenv()
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# ── PHASE 1: INPUT & SANITIZATION ───────────────────────────
def get_clean_input():
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    return clean_input

# ── PHASE 2: PROCESS (Hybrid Intent Matching) ────────────────
def get_response(user_input):
    # First → check the rule-based dictionary (O(1) instant lookup)
    if user_input in responses:
        print("  [Rule Match ✅]")
        return responses[user_input]

    # No match → hand off to Groq LLM
    print("  [No Rule Found → Asking Groq LLM... 🤖]")
    return ask_llm(user_input)

# ── LLM FALLBACK ─────────────────────────────────────────────
def ask_llm(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Keep your answers short and clear."
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama-3.3-70b-versatile",  # free model on Groq
        )
        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"LLM Error: {e}"

# ── PHASE 3: OUTPUT ──────────────────────────────────────────
def display_response(reply):
    print(f"RuleBot: {reply}\n")

# ── THE HEARTBEAT: INFINITE LOOP ─────────────────────────────
def run_chatbot():
    print("=" * 55)
    print("   Welcome to RuleBot — Hybrid Edition")
    print("   Rule-based speed  +  LLM flexibility")
    print("   Type 'exit' or 'quit' to stop.")
    print("=" * 55)
    print()

    while True:
        user_input = get_clean_input()

        if user_input in ("exit", "quit"):
            print("RuleBot: Shutting down... Goodbye! 👋")
            break

        if user_input == "":
            print("RuleBot: Please type something!\n")
            continue

        reply = get_response(user_input)
        display_response(reply)

# ── ENTRY POINT ──────────────────────────────────────────────
if __name__ == "__main__":
    run_chatbot()
