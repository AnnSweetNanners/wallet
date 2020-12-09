import subprocess
import json
from constants import *
import os
from dotenv import load_dotenv
load_dotenv()

mnemonic=os.getenv('mnemonic')
# print(mnemonic)

# print(BTC, ETH, BTCTEST)
# command = f'./derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --format=json'

command = f'php derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)
