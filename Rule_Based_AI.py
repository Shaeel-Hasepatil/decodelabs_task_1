#This file is part of the Project-1 The Rule-Based AI chatBox for Week-1 in the Decode Lab Internship dated 25/5/26 to 25/6/26.

#Dictionary- Based on 20+ Intends
response = {
     # Greetings
    "hello":       "Hey there! I'm RuleBot. How can I help you today?",
    "hi":          "Hi! Great to meet you. What's on your mind?",
    "hey":         "Hey! What can I do for you?",
 
    # Farewells
    "bye":         "Goodbye! Have a great day!",
    "goodbye":     "See you later! Take care!",
    "see you":     "See you! Come back anytime.",
 
    # How are you
    "how are you": "I'm just a bunch of if-else logic, but I'm doing great!",
    "what's up":   "Not much — just waiting for your next message!",
 
    # About the bot
    "who are you": "I'm RuleBot, a rule-based chatbot built for DecodeLabs Project 1.",
    "what can you do": "I can respond to greetings, answer basic questions, and chat a little. I'm rule-based, so I only know what I've been taught!",
 
    # Help
    "help":        "Try saying: hello, how are you, who are you, what is ai, joke, or bye.",
 
    # AI topic (relevant to the internship!)
    "what is ai":  "AI stands for Artificial Intelligence — teaching machines to simulate human decision-making.",
    "what is ml":  "Machine Learning is a subset of AI where systems learn from data instead of explicit rules.",
    "what is python": "Python is a beginner-friendly programming language — and a great choice for AI projects!",
 
    # Fun
    "joke":        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "tell me a joke": "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. 😄",
    "what is the meaning of life": "42. (At least, that's what the rule says.)",
} 

#INPUT & SANITIZATION: Inputs and handles case and Whitespaces.
def get_clean_input():
    """Converts the input in lower case and stip's it"""
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    return clean_input

#GENERATE RESPONSE OR FALLBACK: Intent Matching
def get_response(user_input):
    return response.get(user_input,"I don't understand that yet. Try typing 'help'!")

#DISPLAY OUTPUT: Prints the generated response
def display_response(reply):
    print(f"RuleBot: {reply}\n")

#INFINITE LOOP: INPUTs until exit command
def Rule_chatBot():
    print("-"*50)
    print("   Welcome to RuleBot")
    print("   Type 'exit' to stop the bot and 'help' to know avaliable prompts")
    print("-"*50,"\n")

    while True:
        user_input = get_clean_input()

        #KILL Command
        if(user_input == "exit"):
            print("RuleBot: Shutting down... Goodbye! 👋")
            break

        # Skip empty input
        if user_input == "":
            print("RuleBot: Please type something!\n")
            continue

        # Get and display the response
        reply = get_response(user_input)
        display_response(reply)

if __name__ == "__main__":
    Rule_chatBot()

