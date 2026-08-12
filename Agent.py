#create simple chatbot
def simple_chatbot():
    import random

print("Hello! I am NexaBot AI. How can I help you today?")

jokes = [
    # my contributions
    "Why did the computer go to the doctor? Because it had a virus! 🦠😂",

    "Why was the computer cold? Because it left its Windows open!😂"

    "Why do programmers hate nature? It has too many bugs! 🐛😂",

    "What do you call a computer that sings? A-Dell! 🎵😂"
]

while True:
    user_input = input("You: ").lower()

    if user_input in ['exit', 'quit', 'bye']:
        print("NexaBot AI: Goodbye!")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("NexaBot AI: Hello! Nice to meet you.")

    elif "how are you" in user_input:
        print("NexaBot AI: I am doing great! How about you?")

    elif "your name" in user_input:
        print("NexaBot AI: My name is NexaBot AI.")

    elif "calculate" in user_input:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("NexaBot AI:", num1 + num2)

        elif operator == "-":
            print("NexaBot AI:", num1 - num2)

        elif operator == "*":
            print("NexaBot AI:", num1 * num2)

        elif operator == "/":
            if num2 != 0:
                print("NexaBot AI:", num1 / num2)
            else:
                print("NexaBot AI: Cannot divide by zero.")

        else:
            print("NexaBot AI: Invalid operator.")

    elif "joke" in user_input:
        print("NexaBot AI:", random.choice(jokes))

    elif "thank" in user_input:
        print("NexaBot AI: You're welcome!")

    else:
        print(f"NexaBot AI: You said '{user_input}'. That's interesting!")