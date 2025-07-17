import os
import time
from dotenv import load_dotenv
from web3 import Web3
from utils.tokens import get_token_contracts, get_token_balance
from utils.dex import find_arbitrage_opportunity, execute_trade
from utils.logger import log_info, log_trade

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("WALLET")

w3 = Web3(Web3.HTTPProvider(RPC_URL))
WALLET = Web3.to_checksum_address(WALLET_ADDRESS)

TOKEN_LIST = ["XRP", "ADA", "BNB", "SOL"]
TOKEN_CONTRACTS = get_token_contracts(w3, TOKEN_LIST)

while True:
    for symbol in TOKEN_LIST:
        token = TOKEN_CONTRACTS[symbol]
        balance = get_token_balance(w3, token, WALLET)

        opportunity = find_arbitrage_opportunity(w3, token, symbol)
        if opportunity and opportunity['profit'] >= 0.2:
            log_info(f"[OPORTUNIDADE] {symbol} - Lucro estimado: {opportunity['profit']} USDT")
            success, tx_hash = execute_trade(w3, token, symbol, opportunity, PRIVATE_KEY, WALLET)
            if success:
                log_trade(symbol, opportunity, tx_hash)
        else:
            log_info(f"Nenhuma oportunidade para {symbol} detectada.")

    time.sleep(10)
