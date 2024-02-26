import json
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SmsHub API key (obtained from https://smshub.org/)
APIKEY = os.getenv('SMSHUB_API')
# Main URL for SmsHub API requests
MAIN_URL = f'https://smshub.org/stubs/handler_api.php?api_key={APIKEY}&action='

# Constants for setting status
CANCEL_NUMBER = 8
GET_NEW_CODE = 3
FINISH_NUMBER = 6

# Path to file smshub service
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'service.txt')

# Read data from text files
with open(file_path, 'r') as file:
    SERVICES_DICT = json.load(file)

# Load the dictionary of services and their corresponding codes
# from the file
if SERVICES_DICT:
    SERVICES = SERVICES_DICT
else:
    EXAMPLE_DICT = {
        'Service name': 'Service code',
    }
    SERVICES = EXAMPLE_DICT

# Telegram bot token (obtained from https://core.telegram.org/bots/api)
BotToken = os.getenv('BOT_TOKEN')
