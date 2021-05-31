import logging
import sys
import os

from web3 import Web3


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

ganache = 'http://127.0.0.1:8545'

def main():


    logging.info('Getting Blockchain Info')

    w3 = Web3(Web3.HTTPProvider(ganache))

    logging.info('current Web3 version: {}'.format(w3.api))
    logging.info('current client version: {}'.format(w3.clientVersion))

    logging.info('w3.isConnected(): {}'.format(w3.isConnected()))

    logging.info('Getting the latest block')
    w3.eth.get_block('latest')

    logging.info('eth_accounts')
    w3.eth.get_accounts()


if __name__ == '__main__':
    main()
