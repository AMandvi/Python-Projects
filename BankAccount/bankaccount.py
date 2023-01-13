class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance=0): 
        self.int_rate= int_rate
        self.balance= balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance+=amount
        return self

    def withdraw(self, amount):
        if self.balance<amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        else:
            self.balance-=amount
        return self


    def display_account_info(self):
        print(f"Balance : ${self.balance}")
        return self

    def yield_interest(self):
        self.balance += self.balance*self.int_rate
        return self

bankAccount1 = BankAccount(.01, 1000)
bankAccount2 = BankAccount(.50, 450)

bankAccount1.deposit(10).deposit(20).deposit(30).withdraw(500).yield_interest().display_account_info()
bankAccount2.deposit(100).deposit(200).withdraw(10).withdraw(40).withdraw(100).yield_interest().display_account_info()
