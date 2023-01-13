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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=100)
        # self.account2 = BankAccount(.50, 100)
    
    
    def make_deposit(self, amount,bank):
        self.account.deposit(amount)
        # if (bankAccountName == "account"):
        #     self.account.deposit(amount)  
        # elif (bankAccountName == "account2"):
        #     self.account2.deposit(amount)

    def make_withdrawl(self,amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        self.account.display_account_info()


user1 = User("Mandvi", "t@t.com")
user1.make_deposit(10)
user1.make_withdrawl(30)
user1.display_user_balance()
