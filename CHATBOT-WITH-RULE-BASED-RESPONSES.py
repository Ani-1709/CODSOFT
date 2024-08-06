def chatbot_response(user_input):
    # Convert user input to lower case for case-insensitive matching
    user_input = user_input.lower()

    # Predefined responses based on user queries
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a chatbot, but I'm doing great! How about you?"
    elif "what is your name" in user_input:
        return "I'm ChatBot, your virtual assistant."
    elif "help" in user_input:
        return "Sure, I'm here to help! What do you need assistance with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main loop to interact with the chatbot
def chat():
    print("ChatBot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")
        if "bye" in user_input.lower() or "goodbye" in user_input.lower():
            break

# Start the chat
chat()
