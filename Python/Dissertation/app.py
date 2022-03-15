import json
from web3 import Web3

abi = json.load('[{"inputs":[],"name":"retrieve","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"num","type":"uint256"}],"name":"store","outputs":[],"stateMutability":"nonpayable","type":"function"}]')


address = web3.toChecksumAddress('0xe458c6f2e70e533d341f2dd6e681b5b3be5bc934')

infura_url = "https://kovan.infura.io/v3/0fd565c546e54ecea520208e320469e1"

web3 = Web3(Web3.HTTPProvider(infura_url))


