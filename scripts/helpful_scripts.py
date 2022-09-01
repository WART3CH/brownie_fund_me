from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3  # helps import functionality like toWei(Read More!!!)

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "ganache-local",
]  # LOCAL_BLOCKCHAIN_ENVIRONMENT is a flag to extend the definition of or development networks

DECIMALS = 8  # static variable
STARTING_PRICE = 200000000000  # static variable


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"the active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMALS,
            Web3.toWei(STARTING_PRICE, "ether"),
            {"from": get_account()},  # toWei will help us get rid of the clunky zeros.
        )
    price_feed_address = MockV3Aggregator[
        -1
    ].address  # [-1] > use the most recently deployed MockV3Aggregator
    print("Mock Deployed!!!")
