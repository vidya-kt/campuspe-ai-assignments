balance = 500
history = []

while True:
    print("\nATM SIMULATOR")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you! Exiting.....")
        break

    elif choice == "1":
        print("Your Account Balance is: ₹", balance)
        history.append("Checked balance: ₹ " + str(balance))

    elif choice == "2":
        deposit_amt = int(input("Enter the amount to deposit: "))
        if deposit_amt <= 0:
            print("Invalid amount!")
        else:
            balance += deposit_amt
            print("Deposit successful!")
            print("Updated Balance: ₹", balance)
            history.append("Deposited ₹ " + str(deposit_amt))

    elif choice == "3":
        withdraw_amt = int(input("Enter the amount to withdraw: "))

        if withdraw_amt <= 0:
            print("Invalid amount!")

        elif withdraw_amt > balance:
            print("Insufficient balance. Withdrawal failed!")

        elif balance - withdraw_amt < 500:
            print("Minimum balance of ₹500 must be maintained. Withdrawal denied!")

        else:
            balance -= withdraw_amt
            print("Withdrawal successful!")
            print("New balance: ₹", balance)
            history.append("Withdrew ₹ " + str(withdraw_amt))

    #Transaction History
    elif choice == "4":
        print("\n--- Transaction History ---")
        if len(history) == 0:
            print("No transactions yet")
        else:
            for h in history:
                print(h)

    else:
        print("Invalid choice! Please select between 1 and 5.")