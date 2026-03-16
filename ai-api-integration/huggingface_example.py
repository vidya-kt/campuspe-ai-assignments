# huggingface_example.py

# 1.API Configuration
import requests
import os

API_URL = "https://router.huggingface.co/v1/chat/completions"
HF_TOKEN = os.getenv("HF_TOKEN")

headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


# 2.Query Function
def query_api(prompt):
    try:
        data = {
            "model": "meta-llama/Meta-Llama-3-8B-Instruct",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 500
        }

        response = requests.post(API_URL, headers=headers, json=data)
        result = response.json()

        return result["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"


# 3.Main Execution
if __name__ == "__main__":

    print("Hugging Face Chat App (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        reply = query_api(user_input)
        print("Bot:", reply)