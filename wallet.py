import subprocess
import json
from constants import *
import os
from dotenv import load_dotenv
load_dotenv()
jsonnum=[]

# print(BTC, ETH, BTCTEST)

mnemonic=os.getenv('mnemonic')
# print(mnemonic)

# command = f'./derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --format=json'

def derive_wallet(mnemonic, coin, numderive):
    command = f'php derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --coin="{coin}" --numderive="{numderive}" --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    keys = json.loads(output)
    return print(keys)
    

derive_wallet(mnemonic, ETH, 3)
derive_wallet(mnemonic, BTC, 4)
derive_wallet(mnemonic, BTCTEST,3)