class BankAccount:
    name="Raghu"
    accnum=110126835213
    balance=5000
    def deposit(self,amount):
        amount=self.balance + amount
        print(amount)
    def withdrawl(self,cash):
        cash=self.balance - cash
        print(cash)
    def display_balance(self):
        print("Total Balance is : ",self.balance)
        
b=BankAccount()
b.deposit(10000)
b.withdrawl(2000)
b.display_balance()
        