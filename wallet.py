import subprocess
import json
from constants import *
import os
from dotenv import load_dotenv
from web3 import Web3
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from eth_account import Account
from bit import wif_to_key


load_dotenv()

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

mnemonic=os.getenv('mnemonic')

def derive_wallet(mnemonic, coin_type, numderive):
    command = f'php derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --coin="{coin_type}" --numderive="{numderive}" --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return keys
    
coins={ETH:derive_wallet(mnemonic, ETH, 3), BTCTEST:derive_wallet(mnemonic, BTCTEST, 3)}

coins[ETH][0]['privkey']
print(coins[BTCTEST])

def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return (Account.privateKeyToAccount(priv_key))
    elif coin == BTCTEST:
        return (PrivateKeyTestnet(priv_key))
    else:
        raise Exception('Choose eth or btc-test')
    
priv_key_to_account(ETH, coins[ETH][0]['privkey'])

def create_raw_tx(coin, account, recipient, amount):
    if coin==ETH:
        
        gasEstimate = w3.eth.estimateGas(
            {"from": account.address, "to": recipient, "value": amount}
        )
        return {
            "from": account.address,
            "to": recipient,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(account.address),
        }
    
    elif coin==BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])
    
    else:
        raise Exception('Choose eth or btc-test')
        

def send_tx(coin, account, recipient, amount):
    tx = create_raw_tx(coin, account, recipient, amount)
    if coin==ETH:
        signed_tx = account.sign_transaction(tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
        return result
    elif coin==BTCTEST:
        tx_hex = account.sign_transaction(tx)
        return NetworkAPI.broadcast_tx_testnet(tx_hex)
    else:
        raise Exception('Choose eth or btc-test')
        
# send_tx(BTCTEST, priv_key_to_account(BTCTEST, coins[BTCTEST][0]['privkey']), coins[BTCTEST][1]['address'], .00001)
send_tx(ETH, priv_key_to_account(ETH, coins[ETH][0]['privkey']), coins[ETH][1]['address'], 35000000000000000000)


