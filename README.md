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

# II. Adding HD Wallet Derive
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
3. Run the command to cd into hd-wallet-derive
4. Execute the following command:
  - ./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c --numderive=3 --preset=bitcoincore --cols=path,address --path-change

  You should see something similar once complete:
  ![Verify HD Wallet Working](Screenshots\verify_hd_wallet.png)

 5. Once verified open *Administrator* Bash and cd to Block-chain tools and runt he following:

  * export MSYS=winsymlinks:nativestrict
  * ln -s hd-wallet-derive/hd-wallet-derive.php derive

  To verify it's working type the following two commands into your command line:
  * export MSYS=winsymlinks:nativestrict
  * ln -s hd-wallet-derive/hd-wallet-derive.php derive

  Test that it's working by entering:
  * ./derive -g --mnemonic="YOU'RE MNEMONIC HERE" --cols=path,address,privkey,pubkey

  It should look  like:
  ![derive test](Screenshots\derive_working.png)

  Refer to [this document](requirements.txt) for additional instruction on installing additional dependencies.

#  III. Executing wallet.py

To send Ether, use the following command:

*Note - sends 35 Ether between your 1st and 2nd addresses*

    - send_tx(ETH, priv_key_to_account(ETH, coins[ETH][0]['privkey']), coins[ETH][1]['address'], 35000000000000000000)

![Test Ether Confirmation](Screenshots/ETH.png)

To send TEST BTC, use the following command:

*Note sends .00038928 Test BTC coins between your first and 2nd addresses* 


    - send_tx(BTCTEST, priv_key_to_account(BTCTEST, coins[BTCTEST][0]['privkey']), coins[BTCTEST][1]['address'], .00001)

![Test BTC Confirmation](Screenshots/BTCTEST.png)

# IV. Next steps 
Next steps would be to test the code for other coin types to enhance to functionality of the wallet.