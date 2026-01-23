class Transaction:



    def __init__(self,txn_type,amount,balance):

        self.txn_type = txn_type
        self.amount = amount
        self.balance = balance





class Employee:





    def __init__(self,name,acc_no,balance,bank_branch):
        self.name = name
        self.acc_no = acc_no
        self.bank_branch = bank_branch
        self.balance = balance
        self.transactions = []
        self.history = {}


    def deposit(self,amount):

        if amount<=0:
            return

        self.balance+=amount;
        print("amount deposited successfully")
        self.transactions.append(Transaction("deposit",amount,self.balance))
        self.history["deposit"] = {amount}


    def widthdrawal(self,amount):

        if self.balance<0 and amount>self.balance and amount<0:
            return


        self.balance-=amount
        print("amount widhdrawed successfully")
        self.transactions.append(Transaction("widthdraw",amount,self.balance))
        self.history["widthdrawal"] = {amount}







