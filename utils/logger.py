def log_info(msg):
    print(f"[INFO] {msg}")

def log_trade(symbol, opportunity, tx_hash):
    print(f"[TRADE] Token: {symbol} | DEX Buy: {opportunity['dex_buy']} | DEX Sell: {opportunity['dex_sell']}")
    print(f"[TX] Hash: {tx_hash} | Lucro estimado: {opportunity['profit']} USDT")
