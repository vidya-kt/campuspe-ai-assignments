# cohere_example.py

# 1.API Configuration
import cohere
import os

api_key = os.getenv("COHERE_API_KEY")   # API key from environment variable
co = cohere.Client(api_key)

chat_history = []


# 2.Query Function
def query_api(prompt):
    try:
        response = co.chat(
            model="command-a-03-2025",
            message=prompt,
            chat_history=chat_history
        )

        reply = response.text

        chat_history.append({"role": "USER", "message": prompt})
        chat_history.append({"role": "CHATBOT", "message": reply})

        return reply

    except Exception as e:
        return f"Error: {str(e)}"


# 3.Main Execution
if __name__ == "__main__":

    print("Cohere Chatbot (type 'exit' to stop)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        result = query_api(user_input)
        print("Bot:", result)