from brownie import accounts, Dracarys
from web3 import Web3

initial_supply = Web3.toWei(100000, "ether")


def deploy():
    account = accounts.load("MyAccount")
    dracarys = Dracarys.deploy(initial_supply, {"from": account}, publish_source=True)


def main():
    deploy()
