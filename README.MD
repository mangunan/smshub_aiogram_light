# SMSHub-API-Telegram-Bot

This project demonstrates a Telegram Bot designed to interact with the smshub.org API for managing phone numbers. It provides a simple and convenient interface for viewing balance, buying numbers, and managing status (cancellation, getting a new code, finishing the number). It is implemented using Python, aiogram, and asyncio.

## Features

- Get balance from your smshub.org account.
- Buy phone numbers from various services.
- Cancel numbers, get new codes, and finish numbers.
- Convenient user interface using Telegram Bot.
- Restrict access to the bot only to your own Telegram ID.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need Python 3.8 or later to run the bot. You can have multiple Python versions (2.x and 3.x) installed on the same system without problems.

In Ubuntu, Mint, and Debian you can install Python like this:

```bash
sudo apt-get install python3 python3-pip
```

For other Linux flavors, macOS, and Windows, packages are available at

http://www.python.org/getit/

.
### Quick Start

Clone the repository:

```bash
git clone https://github.com/mangunan/smshub_aiogram_light.git
cd smshub_aiogram_light
```

Create a virtual environment to isolate your dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the python dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and update the content:

```bash
cp .env.example .env
nano .env
```

Your `.env` file should look like this:

```bash
SMSHUB_API=your_sms_hub_api_key
BOT_TOKEN=your_telegram_bot_token
MY_CHAT_ID=your_telegram_chat_id_1,your_telegram_chat_id_2,your_telegram_chat_id_3
```


To get your Telegram Chat ID, you can use [@userinfobot](https://t.me/userinfobot) on Telegram. Simply forward a message to this bot, and it will reply with the user info, including the Chat ID.

.
### Configuring the service list

You can get the list of Service Name and code in https://smshub.org/en/info#getServices

Edit the `service.txt`

```bash
{
  "Service Name": "code",
  "Service Name2: "code2",
}
```

.
### Running the Bot

To start the bot, run the following command:

```bash
python3 main.py
```

Now, you can go to your Telegram App and interact with your bot.

.
### Autostart the bot

To make bot autorun when system is booting

Make service, command:

```bash
sudo nano /etc/systemd/system/smshub.service
```

Put this, change username with your username

```bash
[Unit]
Description=SMSHub BOT service

[Service]
WorkingDirectory=/home/username/smshub_aiogram_light
ExecStart=/home/username/smshub_aiogram_light/venv/bin/python3 main.py
User=username
Type=simple
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```


Then reload and enable the service

```bash
sudo systemctl daemon-reload
sudo systemctl enable smshub.service
sudo systemctl start smshub
sudo systemctl status smshub
```


Now you should see the service is running OK


## Usage

- Use `/start` command to initiate interaction with the bot.
- Click on '💵 Balance' to get the balance from your smshub.org account.
- Click on '📞 Buy number' to buy a phone number from a list of available services.
- When a number is bought, you can click 'Cancel' to cancel the number, 'Get new code' to get a new code for the number, and 'Finish' to mark the number as finished.

## Configure Operator, Country ID, and Max Price

This script already modified for better usage of IDN number, if you want change the country number, go to `smshub_api/api.py` and goto `line 37`

```bash
async def get_number(self, service, country=6):
```

6 for IDN, 0 for any

Other country code you can see in https://smshub.org/en/info#getCountries

For the operator, you can edit `smshub_api/api.py` in `line 47` add param `&operator=`

```
url = f'{self.main_url}getNumber&service={service}&country={country}&operator=any
```

You can set the max price in the bot too, but i prefer set max price in the smshub website, the bot will follow automatically, so you dont need to edit manually

If you prefer set max price in the bot, just edit `smshub_api/api.py` in `line 47` add param `&maxPrice=`


## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- [aiogram](https://github.com/aiogram/aiogram): An async Python framework for Telegram Bot API.
- [httpx](https://github.com/encode/httpx): A fully featured HTTP client for Python 3.6+.
