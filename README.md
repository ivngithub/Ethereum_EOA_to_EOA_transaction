# Ethereum_EOA_to_EOA_transaction

```
python3 -m venv venv
source ./venv/bin/activate
export ETH_ADD1=0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318
export ETH_ADD2=0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362317
export ETH_BALANCE=99999999999999999
docker run --detach --publish 8545:8545 trufflesuite/ganache-cli:latest --account="$ETH_ADD1,$ETH_BALANCE" --account="$ETH_ADD2,$ETH_BALANCE"
python eoa_to_eoa_transaction.py
```
