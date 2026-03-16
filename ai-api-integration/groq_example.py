# groq_chat_app.py

# 1. API Configuration
from groq import Groq
import os

# Get API key from environment variable
api_key = os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)

# 2. Query Function
def query_api(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant"
        )

        reply = chat_completion.choices[0].message.content
        return reply

    except Exception as e:
        return f"Error: {str(e)}"

# 3. Main Execution
if __name__ == "__main__":

    print("AI Chat App (type 'exit' to stop)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Chat ended.")
            break

        print("Querying API...")

        result = query_api(user_input)

        print("AI:", result)