# wallet
Multi-Blockchain Wallet in Python

This code creates a 'universal' wallet that manages multiple crypto coins allowing for portfolio-like management of multiple coins. For this test, I used Ethereum and Bitcoin Testnet. This code uses a command line tool, hd-wallet-derive that supports BIP32, BIP39, and BIP44 as well as non-standard derivation paths.

# I. Dependencies
* subprocess
* json
* os
* dotenv
* web3
* bit
* constants.py
* ganache

## Adding HD Wallet Derive
The hd-wallet-derive library is written in the PHP language. PHP should be installed for hd-wallet-derive to work. To install hd-wallet-derive:
1. Open a fresh terminal as *Administrator*.
    - Input "C:\Program Files\Git\bin\bash.exe directly into the system search bar and launch as *Administrator*.

2. With your terminal open, cd into your 'Blockchain-Tools' folder and run the following code:
  - git clone https://github.com/dan-da/hd-wallet-derive
  - cd hd-wallet-derive
  - curl https://getcomposer.org/installer -o installer.php
  - php installer.php
  - php composer.phar install

  You should now have a folder called hd-wallet-derive! To verify it is functioning:
1. Run the command to cd into hd-wallet-derive
2. Execute the following command:
  - ./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c --numderive=3 --preset=bitcoincore --cols=path,address --path-change

  You should see something similar once complete:
  ![Derive Working](Screenshots\Derive_working.png)

