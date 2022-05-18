# Potential Attributes a wallet could have
# current amount in the wallet

# Potential Methods a wallet could have
# adding or subtracting money
# spend money
# adding money


class Wallet:
    # Class Constructor
    # Class initialization 
    def __init__(self, initial_amount=0):
        # store the user-provided initial_amount as an attribute
        self.balance = initial_amount

    # Methods Will only be executed when they are called
    # after the class has already been instantiated

    def spend_cash(self, amount):
        # check to see if we have enough money
        if self.balance <= amount:
            return "you can't afford it!"
        else:
            # self.balance = (self.balance - amount)
            self.balance -= amount
            return "you can afford it!"


    def add_cash(self, amount):
        # self.balance = (self.balance + amount)
        self.balance += amount
        return f"Added ${amount} dollars to the wallet"

    # PRACTICE USING THE __REPR__ Function
    # you will need to use it on the Sprint Challenge
    def __repr__(self):
        return f"<Wallet - Balance: ${self.balance}>"


if __name__ == '__main__':
    ryans_wallet = Wallet()
    josh_wallet = Wallet(100)
    # print(ryans_wallet.balance)
    # print(josh_wallet.balance)

    # print(josh_wallet.spend_cash(10))
    # print(josh_wallet.balance)
    # print(josh_wallet.spend_cash(100))

    # print(ryans_wallet.add_cash(9999999999999))
    # print(ryans_wallet.balance)
    # print(ryans_wallet.spend_cash(1234566543))
    # print(ryans_wallet.balance)

    print([ryans_wallet, ryans_wallet, ryans_wallet, ryans_wallet])
    # print(ryans_wallet)
    # print(ryans_wallet)
    # print(ryans_wallet)


