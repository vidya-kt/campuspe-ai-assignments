#multi_api_query.py

#1.API Configuration
import os
import requests
import google.generativeai as genai
import cohere
from groq import Groq

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-2.5-flash")

co = cohere.Client(os.getenv("COHERE_API_KEY"))

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

HF_TOKEN = os.getenv("HF_TOKEN")
hf_url = "https://router.huggingface.co/v1/chat/completions"
hf_headers = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

ollama_url = "http://localhost:11434/api/generate"


#2.Query Function
def query_api(provider, prompt):
    try:
        if provider == "1":
            response = gemini_model.generate_content(prompt)
            return response.text

        elif provider == "2":
            response = co.chat(model="command-a-03-2025", message=prompt)
            return response.text

        elif provider == "3":
            response = groq_client.chat.completions.create(
                messages=[{"role": "user", "content": prompt}],
                model="llama-3.1-8b-instant"
            )
            return response.choices[0].message.content

        elif provider == "4":
            data = {
                "model": "meta-llama/Meta-Llama-3-8B-Instruct",
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(hf_url, headers=hf_headers, json=data)
            return response.json()["choices"][0]["message"]["content"]

        elif provider == "5":
            data = {"model": "llama2", "prompt": prompt, "stream": False}
            response = requests.post(ollama_url, json=data)
            result = response.json()

            if "response" in result:
                return result["response"]
            else:
                return str(result)
        else:
            return "Invalid choice"

    except Exception as e:
        return f"Error: {str(e)}"


#3.Main Execution
if __name__ == "__main__":

    while True:
        print("\nSelect AI Provider")
        print("1. Gemini")
        print("2. Cohere")
        print("3. Groq")
        print("4. HuggingFace")
        print("5. Ollama")
        print("Type 'exit' to quit")

        choice = input("Enter choice: ")

        if choice.lower() == "exit":
            break

        prompt = input("Enter your prompt: ")

        reply = query_api(choice, prompt)

        print("AI:", reply)