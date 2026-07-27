def withdraw(balance,transaction):
                withdraw_amount = float(input("Enter the amount you want to withdraw: "))
                if balance < withdraw_amount:
                    print("Insufficient funds!")
                    transaction.append(f"Withdraw: Failed")
                    return balance
                else :
                    balance-=withdraw_amount;
                    print(f"Balance: {balance}")
                    transaction.append(f"Withdrew: {withdraw_amount}")
                    return balance

def deposit(balance,transaction):
    deposited_amount = float(input("Enter the amount you want to deposit: "))
    balance+=deposited_amount
    transaction.append(f"Deposited: {deposited_amount}")
    print(f"Balance: {balance}")
    return balance

def viewbalance(balance):
     print(f"Balance: {balance}")

def transactionhistory(transaction):
     j=1
     for i in transaction:
      print(j,i,"\n")
      j+=1
     

def atmfunction():
    transaction = []
    id = {}
    name = input("Enter your name...\n")
    if name in id:
             print("You are a registered user....")
    else :
                balance = float(input("Youre name is not present as a registered user, add your balance and will be registered...\n"))
                id[name] = balance
                print(id)   
    while True:

        choice = input("Enter:\n1 to view balance:\n2 to deposit:\n3 to withdraw:\n4.View transaction history:\n0 to exit:\n")
        if choice.isdigit() == False:
            print("Invalid choice")
            continue
        choice = int(choice)
        if choice == 2: #DEPOSIT
            id[name] = deposit(id[name],transaction)

        elif choice == 1:
            viewbalance(id[name])

        elif choice == 3: #WITHDRAW
            id[name] = withdraw(id[name],transaction)

        elif choice == 0:
            print("exited successfully....")
            break

        elif choice == 4:
            transactionhistory(transaction)
        else :
            print("invalid choice:")

atmfunction()