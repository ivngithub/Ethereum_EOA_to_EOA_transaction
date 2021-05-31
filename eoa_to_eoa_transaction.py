import logging
import sys
import os

from web3 import Web3


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

ganache = 'http://127.0.0.1:8545'
privet_keys = (os.environ['ETH_ADD1'], os.environ['ETH_ADD2'])


def main():

    logging.info('Sign a Transaction')

    w3 = Web3(Web3.HTTPProvider(ganache))

    current_block = w3.eth.get_block('latest')
    accounts = w3.eth.get_accounts()
    print(current_block)

    transaction = {
        'to': accounts[1],
        'value': 100,
        'gas': 2000000,
        'gasPrice': 2,
        'nonce': 0,
        'chainId': current_block['number'] + 1
    }

    key = privet_keys[0]
    signed = w3.eth.account.sign_transaction(transaction, key)
    logging.info('signed.rawTransaction: {}'.format(signed.rawTransaction))
    logging.info('signed.hash: {}'.format(signed.hash))
    logging.info('signed.r: {}'.format(signed.r))
    logging.info('signed.s: {}'.format(signed.s))
    logging.info('signed.v: {}'.format(signed.v))

    logging.info('Send a Transaction')
    w3.eth.send_raw_transaction(signed.rawTransaction)

    logging.info('Get Balance Fore Recipient')
    logging.info('{}'.format(w3.eth.getBalance(accounts[1])))


if __name__ == '__main__':

    main()
