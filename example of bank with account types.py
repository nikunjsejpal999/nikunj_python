class Bank:
    
    def openaccount(self, cname, acno, balance):
        self.cname = cname
        self.acno = acno
        self.balance = balance  # Store balance as an instance variable
        print(f"Hello {cname}, your account number is {acno} with initial balance of {balance} rs.")
    
    def deposite(self, amount):
        self.balance += amount  # Update the balance with the deposit
        print(f"Your balance is: {self.balance} rs.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount  # Deduct from the balance if sufficient funds are available
            print(f"Your balance is: {self.balance} rs.")
        else:
            print("You have insufficient balance.")

    def checkbalance(self):
        print(f"Your available balance is: {self.balance} rs.")

b1 = Bank()

while True:
    print("\n1. Open account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cname = input("Enter your name: ")
        acno = int(input("Enter your account number: "))
        balance = int(input("Enter your initial balance: "))
        
        # Account type selection (Saving or Current)
        while True:
            print("1. Saving account")
            print("2. Current account")
            acc_choice = int(input("Enter your choice for account type: "))
            if acc_choice == 1:
                print("Your account type is Saving account.")
            else:
                print("Your account type is Current account.")
            break
        
        b1.openaccount(cname, acno, balance)
    
    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        b1.deposite(amount)
    
    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        b1.withdraw(amount)
    
    elif choice == 4:
        b1.checkbalance()
    
    elif choice == 5:
        break
    else:
        print("Invalid option.")
