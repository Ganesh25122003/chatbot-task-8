# chatbot.py

def chatbot():
    print("Hello! I am your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hi" or user_input == "hello":
            print("Bot: Hello there! How can I help you?")
        
        elif user_input == "how are you":
            print("Bot: I'm doing great, thank you! How about you?")
        
        elif user_input == "fine" or user_input == "good":
            print("Bot: That's nice to hear!")
        
        elif user_input == "what is your name":
            print("Bot: I am a simple rule-based chatbot.")
        
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        
        else:
            print("Bot: Sorry, I don’t understand that.")

if __name__ == "__main__":
    chatbot()