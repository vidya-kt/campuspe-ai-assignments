# gemini_example.py

# 1.API Configuration
import google.generativeai as genai
import os

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


# 2.Query Function
def query_api(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"


# 3.Main Execution
if __name__ == "__main__":

    print("Gemini Chat App (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        reply = query_api(user_input)
        print("Bot:", reply)