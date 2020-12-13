# import os
# os.chdir(r'C:\Users\annmi\OneDrive\Desktop\Class\Homework\wallet')

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
# w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# print(BTC, ETH, BTCTEST)

mnemonic=os.getenv('mnemonic')
# print(mnemonic)

# coin_types=['ETH','BTCTEST']
# coins={}

# command = f'./derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --format=json'

def derive_wallet(mnemonic, coin_type, numderive):
    command = f'php derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --coin="{coin_type}" --numderive="{numderive}" --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return print(keys)
    

# derive_wallet(mnemonic, ETH, 3)
# # derive_wallet(mnemonic, BTC, 4)
# # derive_wallet(mnemonic, BTCTEST,3)

def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return (Account.privateKeyToAccount(priv_key))
    elif coin == BTCTEST:
        return (PrivateKeyTestnet(priv_key))
    else:
        raise Exception('Choose eth or btc-test')
    

def create_raw_tx(coin, account, to, amount):
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
        PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    
    else:
        raise Exception('Choose eth or btc-test')
        

def send_tx(account, recipient, amount):
    tx = create_raw_tx(coin, account, to, amount)
    if coin_type==ETH:
        signed_tx = account.sign_transaction(tx)
        result = w3.eth.sendRawTransaction(signed_tx.rawTransaction)
    elif coin_type==BTCTEST:
        tx_hex = account.sign_transaction(tx)
        return NetworkAPI.broadcast_tx_testnet(tx_hex)
    else:
        raise Exception('Choose eth or btc-test')

#Try Code:
print(f'Trying Code:')
print(f'Getting Wallets:')
print(f'----------------------------')
print(f' ETH Wallet:')
eth_wallet=derive_wallet(mnemonic, ETH, 3)
print(f'----------------------------')
print(f' BTC Wallet:')
btc__test_wallet=derive_wallet(mnemonic, BTCTEST, 3)

print(f'Get Accounts:')

print('Get account for ETH addresses:')
priv_key_to_account(ETH, f'0x37dbd954dae37e8fba1327254591d4aef7641e27b473ad1be034efbca3fe75e5')

print('Get account for BTC-TEST addresses')
priv_key_to_account(BTCTEST, f'cUNVW9fK9WSBY6ULBxtPHLcW6dj3PxAmTZAvAt98iDzq23zpbgfX')
# priv_key_to_account(BTCTEST, f'cUUTakUUvMLecMJB1qKRcroUm6wzFj2fE8CcGTBNbQUdmthNnK5i')


print(f'Testing TXN Code:')


# account=f'mvdKNWWgy4rjBFmWYwUUZQcVRBDU9cXFcp'
# address=f'mvdKNWWgy4rjBFmWYwUUZQcVRBDU9cXFcp'
# to=f'mrEvFFiRBfLiSy26T8nhLfYFyyYaRxbWGs'
# amount=0.00000001

# print('Create Transaction:')
# create_raw_tx(BTCTEST, account, to, amount)

# send_tx(account, recipient, amount):