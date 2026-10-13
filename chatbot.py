"""
CodeAlpha Task 4: Basic Chatbot
A simple rule-based chatbot that replies to predefined inputs.
Type 'bye' to end the conversation.
"""


def get_response(user_input):
    """Return the chatbot's reply for the given user input."""
    text = user_input.lower().strip()

    if text in ("hello", "hi", "hey"):
        return "Hi!"
    elif text == "how are you":
        return "I'm fine, thanks!"
    elif text == "what is your name":
        return "I'm a simple Python chatbot."
    elif text == "help":
        return "Try saying: hello, how are you, what is your name, or bye."
    elif text == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can reply to."


def main():
    print("=== Simple Chatbot ===")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() == "bye":
            break


if __name__ == "__main__":
    main()
