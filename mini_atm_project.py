balance = 1000.50
while True:
    choice = input("Enter 1 to view balance, 2 to deposit, 3 to withdraw, 0 to exit:\n")
    if choice.isdigit() == False:
        print("Invalid choice")
        continue
    if int(choice) == 2:
        deposited_amount = int(input("Enter the amount you want to deposit: "))
        balance+=deposited_amount
        print(f"Balance: {balance}")
    elif int(choice) == 1:
        print(f"Balance: {balance}")
    elif int(choice) == 3:
        withdraw_amount = int(input("Enter the amount you want to withdraw: "))
        if balance < withdraw_amount:
            print("Insufficient funds!")
        else :
            balance-=withdraw_amount;
            print(f"Balance: {balance}")

    elif int(choice) == 0:
        print("exited successfully....")
        break
    else :
        print("invalid choice:")