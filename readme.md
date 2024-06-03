# Macadamia_S010_ARB_CEX_DEX_Sin_Sym BOT

  # Executes Macadamia arbitrage opportunities by continuously fetching balances and prices from multiple 30+ exchanges.

    It finds the highest and lowest prices and executes arbitrage if there's an opportunity.
    
     This code runs in an infinite loop and performs the following steps:
     1. Fetches balances and prices for all exchanges using the `get_balance` function and the `fetch_ticker` method of each exchange.
     2. Finds the highest and lowest prices from the fetched prices.
     3. If the minimum price is less than the maximum price, it determines the indices of the minimum and maximum prices.
     4. Calculates the amount to buy by dividing the balance at the minimum index by the minimum price.
     5. Creates a market buy order on the exchange with the minimum index and a market sell order on the exchange with the maximum index.
     6. Logs the arbitrage opportunity with the names of the exchanges involved.
     7. Sleeps for the specified renewal time in minutes.


# Arbitrage Trading Script Explanation

get_balance(exchange) Function:

This function fetches the total balance in USDT (Tether) for a given exchange.
It uses the fetch_balance() method from the CCXT library to retrieve the account balance.
The balance is returned as a dictionary, and we extract the total USDT balance.
execute_arbitrage() Function:
This function runs an infinite loop to continuously monitor arbitrage opportunities.
Inside the loop:
It fetches balances and prices for all exchanges defined in the exchanges list.
Determines the highest and lowest prices among the exchanges.
If there’s an arbitrage opportunity (i.e., the lowest price is less than the highest price):
Calculates the amount of cryptocurrency to buy based on the balance in the exchange with the lowest price.
Executes a market buy order on the exchange with the lowest price.
Executes a market sell order on the exchange with the highest price.
Logs the arbitrage opportunity.
Sleeps for a specified time (renewal interval) before checking again.
Exchange Configuration (exchange_config.py):
This file contains API keys for various exchanges.
Replace the placeholders ('YOUR_BINANCE_API_KEY', 'YOUR_BINANCE_SECRET_KEY', etc.) with your actual API keys.
Macadamia.py Script:
Initializes exchanges using the configured API keys.
Sets up a dictionary of fees for each exchange.
Defines the trading symbol (e.g., 'BTC/USDT').
Specifies the initial balance in USDT and the renewal time interval.


## Overview
The Macadamia Arbitrage Trading Bot is designed to identify arbitrage opportunities across multiple cryptocurrency exchanges. It leverages the CCXT library to interact with exchanges, fetch balances, and execute trades.

## Prerequisites
1. Python 3.x installed
2. Required Python packages (install using `pip install -r requirements.txt`):
   - ccxt
   - python-telegram-bot

## Configuration
1. Edit `exchange_config.py`:
   - Replace the placeholder API keys with your actual keys for each exchange.
2. Set the desired trading symbol (e.g., BTC/USDT) in `Macadamia.py`.
3. Specify your initial balance in USDT and the renewal time interval (in minutes).

## Usage
1. Run the `Macadamia.py` script:

python Macadamia.py

2. The bot will continuously monitor prices and execute arbitrage trades when opportunities arise.
3. Check the logs for arbitrage opportunities.

## Disclaimer
- Past performance is not indicative of future results.
- Ensure that you have sufficient funds and understand the risks before trading.
- Review and comply with the terms of use for each exchange.


## Telegram Integration

You can access and manage the Macadamia bot via Telegram Messenger. Follow these steps:

1. Create a Telegram bot:
   - Open Telegram and search for the "BotFather" user.
   - Start a chat with BotFather and use the `/newbot` command to create a new bot.
   - Follow the instructions to set a name and username for your bot.
   - Note down the generated API token.

2. Integrate with Macadamia.py:
   - In your Macadamia.py code, add the Telegram bot API token.
   - Implement Telegram bot commands (e.g., `/start`, `/status`, `/stop`) to interact with your bot.
   - Use the `python-telegram-bot` library to handle Telegram interactions.

3. Run your bot:
   - Start your Macadamia.py bot.
   - Chat with your Telegram bot to receive updates, check status, and manage arbitrage activities.

## License
Developed by : Smitajyoyi Adhikari & Team @macadamia 
Contact : (desibewdabbsr@gmail.com, 
imperialbluewisky@gmail.com, 
rumoldmunk@gmail.com)
