print("🤖 Hi, I’m your chatbot!")
print("Type 'bye' anytime to end the chat.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("🤖 Chatbot: Goodbye! Have a great day!")
        break
    elif "hello" in user_input.lower():
        print("🤖 Chatbot: Hello! How are you doing?")
    elif "how are you" in user_input.lower():
        print("🤖 Chatbot: I’m doing great, thanks for asking!")
    elif "help" in user_input.lower():
        print("🤖 Chatbot: I can greet you, chat a little, or say goodbye.")
    else:
        print("🤖 Chatbot: Sorry, I don’t understand that yet.")
