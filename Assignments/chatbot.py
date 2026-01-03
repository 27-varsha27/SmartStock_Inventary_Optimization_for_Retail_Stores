import requests

HF_TOKEN = "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"

MODEL = "meta-llama/Llama-3.1-8B-Instruct"

API_URL = "https://router.huggingface.co/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def ask_bot(user_msg):
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_msg}
        ],
        "max_tokens": 250,
        "temperature": 0.7
    }

    res = requests.post(API_URL, headers=HEADERS, json=payload)

    if res.status_code != 200:
        return f"Error {res.status_code}: {res.text}"

    data = res.json()

    try:
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Parsing error: {e}\nRaw: {data}"

def chat():
    print("🤖 Chatbot is ready! Type 'exit' to quit.\n")
    while True:
        msg = input("You: ")
        if msg.lower() == "exit":
            print("Bot: Bye! 👋")
            break

        reply = ask_bot(msg)
        print("Bot:", reply, "\n")

if __name__ == "__main__":
    chat()
