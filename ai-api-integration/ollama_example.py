#ollama_example.py

# 1.API Configuration
import requests

url = "http://localhost:11434/api/generate"


#2.Query Function
def query_api(prompt):
    try:
        data = {
            "model": "llama2",
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(url, json=data)
        result = response.json()

        return result["response"]

    except Exception as e:
        return f"Error: {str(e)}"


#3.Main Execution
if __name__ == "__main__":

    print("Ollama Chat App (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        reply = query_api(user_input)
        print("Bot:", reply)
