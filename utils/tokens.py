from utils.abi import ERC20_ABI

TOKEN_ADDRESSES = {
    "XRP": "0x1D2F0dA169ceB9Fc7B3144628dB4F9F4f9b09B52",
    "ADA": "0x3EE2200Efb3400fAbB9AacF31297cBdD1d435D47",
    "BNB": "0xB8c540d00dd0Bf76ea12E4B4B95eFC90804f924E",
    "SOL": "0x7DDEE176F665cD201F93eEDE625770E2fD911990",
}

def get_token_contracts(w3, symbols):
    return {symbol: w3.eth.contract(address=w3.to_checksum_address(TOKEN_ADDRESSES[symbol]), abi=ERC20_ABI)
            for symbol in symbols}

def get_token_balance(w3, contract, wallet):
    return w3.from_wei(contract.functions.balanceOf(wallet).call(), 'ether')
