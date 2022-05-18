from bloomdata.wallet import Wallet
import pytest

@pytest.fixture
def empty_wallet():
    '''returns a wallet instance with a zero balance'''
    wallet = Wallet()
    return wallet

@pytest.fixture
def wallet_20():
    '''returns a wallet of balance: 20'''
    return Wallet(20)

def test_empty_wallet(empty_wallet):
    assert empty_wallet.balance == 0

def test_wallet_20(wallet_20):
    assert wallet_20.balance == 20

def test_spend_cash(wallet_20):
    assert wallet_20.spend_cash(50) == "you can't afford it!"
    assert wallet_20.spend_cash(10) == 'you can afford it!'
    assert wallet_20.balance == 10

def test_add_cash(empty_wallet, wallet_20):
    assert empty_wallet.add_cash(50) == 'Added $50 dollars to the wallet'
    assert empty_wallet.balance == 50
    assert wallet_20.add_cash(50) == 'Added $50 dollars to the wallet'
    assert wallet_20.balance == 70