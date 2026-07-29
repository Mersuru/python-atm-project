class bankaccount:

        transaction = []

        def __init__(self,name,balance):
            self.name = name
            self.balance = balance

        def withdraw(self):
            withdraw_amount = float(input("Enter the amount you want to withdraw: "))
            if self.balance < withdraw_amount:
                print("Insufficient funds!")
                self.transaction.append("Withdraw : Failed")
            else :
                self.balance-=withdraw_amount;
                print(f"Balance: {self.balance}")
                self.transaction.append(f"Withdraw : {withdraw_amount}")

        def deposit(self):
            deposited_amount = float(input("Enter the amount you want to deposit: "))
            self.balance+=deposited_amount
            self.transaction.append(f"Deposited : {deposited_amount}")
            print(f"Balance: {self.balance}")

        def viewbalance(self):
         print(f"Balance: {self.balance}")

        def transactionhistory(self):
            j=1
            for i in self.transaction:
                print(j,i,"\n")
                j+=1
        

def atmfunction():
    accounts = {}
    names = []
    while True:
        name = input("Enter your name...\n")
        if name in names:
            print("You are a registered user....")
        else :
            balance = float(input("Youre name is not present as a registered user, add your balance and will be registered...\n"))
            names.append(name)
            accounts[name] = bankaccount(name,balance)

        while True:  
            choice = input("Enter:\n1 to view balance:\n2 to deposit:\n3 to withdraw:\n4.View transaction history:\n0 to exit:\n")
            if choice.isdigit() == False:
                print("Invalid choice")
                continue
            choice = int(choice)
            if choice == 2: #DEPOSIT
                accounts[name].deposit()

            elif choice == 1:
                accounts[name].viewbalance()

            elif choice == 3: #WITHDRAW
                accounts[name].withdraw()

            elif choice == 0:
                print("exited successfully....")
                break

            elif choice == 4:
                accounts[name].transactionhistory()
            else :
                print("invalid choice:")
        
        choice2 = int(input("Enter 0 if you want to exit the atm completely or 1 to log out...\n"))
        if choice2 == 0:
            break
        else :
            continue

        
atmfunction()

# def withdraw(balance,transaction,name):
#     withdraw_amount = float(input("Enter the amount you want to withdraw: "))
#     if balance < withdraw_amount:
#         print("Insufficient funds!")
#         transaction[name].append("Withdraw : Failed")
#         return balance
#     else :
#         balance-=withdraw_amount;
#         print(f"Balance: {balance}")
#         transaction[name].append(f"Withdraw : {withdraw_amount}")
#         return balance

# def deposit(balance,transaction,name):
#     deposited_amount = float(input("Enter the amount you want to deposit: "))
#     balance+=deposited_amount
#     transaction[name].append(f"Deposited : {deposited_amount}")
#     print(f"Balance: {balance}")
#     return balance

# def viewbalance(balance):
#      print(f"Balance: {balance}")

# def transactionhistory(transaction,name):
#      j=1
#      for i in transaction[name]:
#       print(j,i,"\n")
#       j+=1