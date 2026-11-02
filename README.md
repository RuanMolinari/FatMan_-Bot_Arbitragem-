# FatMan — Decentralized Exchange (DEX) Arbitrage Prototype

A Python prototype organized around Web3.py and helper modules for checking token balances, looking for arbitrage opportunities, and submitting transactions on an EVM-compatible network.

## Architecture visible in the repository

- `fatman_executor.py`: loads environment variables, initializes a Web3 connection, prepares a token list, checks balances, asks helper modules for opportunities, and calls the trade-execution function when the configured profit threshold is met.
- `utils/tokens.py`: token contract and balance helpers.
- `utils/dex.py`: DEX opportunity and trade-execution helpers.
- `utils/abi.py`: contract ABI data.
- `utils/logger.py`: logging helpers.

The main loop currently monitors XRP, ADA, BNB, and SOL and uses a configured minimum estimated profit threshold of 0.2 USDT.

## Requirements

- Python 3
- Web3.py
- python-dotenv
- Access to an EVM-compatible RPC endpoint
- Wallet and token configuration appropriate for the selected network

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Configuration

Create a local `.env` file based on `.env.example`:

```env
RPC_URL=https://your-rpc-endpoint
PRIVATE_KEY=your_private_key
WALLET=0xYourWalletAddress
```

**Never commit a real `.env` file, private key, seed phrase, or funded wallet credentials.** Use a dedicated test wallet and a test network while developing. If a real credential has ever been committed or exposed, revoke/rotate it immediately; deleting the file in a later commit does not erase it from Git history.

## Run

```bash
python fatman_executor.py
```

The script enters a continuous polling loop. Review the helper-module implementation and network configuration before running it.

## Status and limitations

This repository should be treated as an experimental prototype, not a production-ready trading system. The README documents the current code structure; it does not claim that profitable trades have been independently verified. Before any live use, the implementation needs comprehensive testing and review of contract addresses, token decimals, liquidity, slippage, gas costs, transaction simulation, nonce management, chain/network validation, error handling, and private-key security.

## Author

Ruan Molinari — [GitHub](https://github.com/RuanMolinari)

## Disclaimer

For educational and software-development purposes only. This is not investment advice. Do not use funds you cannot afford to lose.
