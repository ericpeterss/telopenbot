# OpenAI GPT-Powered Telegram Bot

This is a simple Telegram bot that uses the OpenAI GPT engine to generate conversational responses. The bot takes user input via Telegram and generates a response using the GPT model.

## Requirements

- Python 3.7 or higher
- Python libraries: `openai`, `requests`

## Installation

1. Clone this repository:

'''sh
git clone https://github.com/ericpeterss/telopenbot.git
cd telopenbot
'''

2. Install the required Python packages:

'''sh
pip install -r requirements.txt
'''

3. Set up your OpenAI API key as an environment variable:

'''sh
export OPENAI_API_KEY=your_openai_api_key
'''

4. Set up your Telegram bot token as an environment variable:

'''sh
export TELEGRAM_TOKEN=your_telegram_bot_token
'''

## Usage

To run the bot, simply execute the following command:

'''sh
python main.py
'''

The bot should now be running and able to respond to messages sent via Telegram.

## Configuration

The bot is configured to use the GPT-3.5-turbo or GPT-4 engine. You can modify the `main.py` file to use a different engine or adjust other settings, such as `max_tokens`.

## Deploying to a server

To deploy the bot to a server, follow the provided instructions for your preferred platform, such as [Azure](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=bash&pivots=python-framework-flask).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
