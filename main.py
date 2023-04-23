import os
import openai
import requests
import json
from time import sleep
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Define a function to send messages through the Telegram API
def send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, data=data)

# Define a function to call the OpenAI API and generate a response
def generate_response(prompt):
    api_url = "https://api.openai.com/v1/chat/completions"

    chat_prompt = (
        "You are a helpful assistant.\n"
        f"User: {prompt}\n"
        "Assistant:"
    )

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }

    data = {
    "model": "gpt-4",    
    #"model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    "max_tokens": 1024,
    "n": 1,
    #"stop": ["\n"],
    "temperature": 1
}

    response = requests.post(api_url, headers=headers, json=data)
    response_json = response.json()
    
    # Print the response JSON to check its structure
    #print(response_json)

    # Extract the text from the response JSON
    return response_json['choices'][0]['message']['content'].strip()

# Create a function to handle updates from the Telegram API:
def handle_updates(updates):
    for update in updates:
        message = update['message']

        # Check if the 'text' key exists in the message dictionary
        if 'text' not in message:
            continue

        text = message['text']
        chat_id = message['chat']['id']

        if text:
            response = generate_response(text)
            send_message(response, chat_id)

# Create a function to fetch new updates from the Telegram API
def fetch_updates(offset=None):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates'
    params = {'timeout': 30, 'offset': offset}
    response = requests.get(url, params=params)
    updates = json.loads(response.text)['result']
    return updates

# Create a loop to keep your bot running and processing new messages
last_processed_update_id = None

while True:
    updates = fetch_updates(offset=last_processed_update_id)
    handle_updates(updates)

    if updates:
        last_processed_update_id = updates[-1]['update_id'] + 1
    sleep(1)
