# Macadamia.py
import ccxt
import time
import logging
import os
from exchange_config import (
    BINANCE_API_KEY,
    BINANCE_SECRET_KEY,
    KUCOIN_API_KEY,
    KUCOIN_SECRET_KEY,
    OKX_API_KEY,
    OKX_SECRET_KEY,
    POLONIEX_API_KEY,
    POLONIEX_SECRET_KEY,
    COINEX_API_KEY,
    COINEX_SECRET_KEY,
    BYBIT_API_KEY,
    BYBIT_SECRET_KEY,
    MEXC_API_KEY,
    MEXC_SECRET_KEY,
    UPBIT_API_KEY,
    UPBIT_SECRET_KEY,
    BINGX_API_KEY,
    BINGX_SECRET_KEY,
    GEMINI_API_KEY,
    GEMINI_SECRET_KEY,
    DEEPCOIN_API_KEY,
    DEEPCOIN_SECRET_KEY,
    XT_API_KEY, 
    XT_SECRET_KEY
)
   

# Exchanges fees Configuration
fees = {
    'binance': {'base': 0, 'quote': 0.001},
    'kucoin': {'base': 0, 'quote': 0.001},
    'okx': {'base': 0, 'quote': 0.001},
    'poloniex': {'base': 0, 'quote': 0.001},
    'coinex': {'base': 0, 'quote': 0.001},
    'bybit': {'base': 0, 'quote': 0.001},
    'mexc': {'base': 0, 'quote': 0.001},
    'upbit': {'base': 0, 'quote': 0.001},
    'bingx': {'base': 0, 'quote': 0.001},
    'gemini': {'base': 0, 'quote': 0.001},
    'deepcoin': {'base': 0, 'quote': 0.001},
    'xt': {'base': 0, 'quote': 0.001},
}


# Initialize exchanges 
exchanges = [
    ccxt.binance({'apiKey': BINANCE_API_KEY, 'secret': BINANCE_SECRET_KEY}),
    ccxt.kucoin({'apiKey': KUCOIN_API_KEY, 'secret': KUCOIN_SECRET_KEY}),
    ccxt.okex({'apiKey': OKX_API_KEY, 'secret': OKX_SECRET_KEY}),
    ccxt.poloniex({'apiKey': POLONIEX_API_KEY, 'secret': POLONIEX_SECRET_KEY}),
    ccxt.coinex({'apiKey': COINEX_API_KEY, 'secret': COINEX_SECRET_KEY}),
    ccxt.bybit({'apiKey': BYBIT_API_KEY, 'secret': BYBIT_SECRET_KEY}),
    ccxt.mexc({'apiKey': MEXC_API_KEY, 'secret': MEXC_SECRET_KEY}),
    ccxt.upbit({'apiKey': UPBIT_API_KEY, 'secret': UPBIT_SECRET_KEY}),
    ccxt.bingx({'apiKey': BINGX_API_KEY, 'secret': BINGX_SECRET_KEY}),
    ccxt.gemini({'apiKey': GEMINI_API_KEY, 'secret': GEMINI_SECRET_KEY}),
    ccxt.deepcoin({'apiKey': DEEPCOIN_API_KEY, 'secret': DEEPCOIN_SECRET_KEY}),
    ccxt.xt({'apiKey': XT_API_KEY, 'secret': XT_SECRET_KEY}),
]

 # Define the symbols and timeframes
symbol = 'BTC/USDT'
initial_balance_usdt = 1000
renew_time_minutes = 30

# Define the arbitrage function
def get_balance(exchange):
    balance = exchange.fetch_balance()
    return balance['total']['USDT']
    
# Arbitrage Function.
def execute_arbitrage():
    while True:
        try:
            # Fetch balances and prices for all exchanges
            balances = [get_balance(ex) for ex in exchanges]
            prices = [ex.fetch_ticker(symbol)['last'] for ex in exchanges]

            # Find the highest and lowest prices
            min_price = min(prices)
            max_price = max(prices)

            # Execute arbitrage if there's an opportunity
            if min_price < max_price:
                min_index = prices.index(min_price)
                max_index = prices.index(max_price)
                amount_to_buy = balances[min_index] / min_price
                exchanges[min_index].create_market_buy_order(symbol, amount_to_buy)
                exchanges[max_index].create_market_sell_order(symbol, amount_to_buy)
                logging.info(f"Arbitrage opportunity: Buy on {exchanges[min_index].name}, sell on {exchanges[max_index].name}")

            time.sleep(renew_time_minutes * 60)

        except ccxt.BaseError as e:
            logging.error(f"Error: {e}")
            time.sleep(10)

if __name__ == '__main__':
    execute_arbitrage()



