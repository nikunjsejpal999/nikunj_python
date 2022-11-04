class Bank:
    
    def openaccount(self,cname,acno,balance):
        print("hello",cname,
              "your account number is",acno,
              "with initial balance",balance,"rs")

    def deposite(self,amount):
        self.b=amount+balance
        print("your  balance is:",self.b)

    def withdraw(self,amount):
        if amount<=self.b:
            self.b=self.b-amount
            print("your balance is:",self.b)

        else:
            print("you have insufficient balance")

    def checkbalance(self):
        print("your availale balance is: ",self.b)

b1=Bank()

while True:
    print("1. openaccount")
    print("2. deposite")
    print("3. withdraw")
    print("4. checkbalance")
    print("5. exit")

    choice=int(input("enter your choice: "))

    if choice==1:
        cname=input("Enter your name:")
        acno=int(input("enter your account number:"))
        balance=int(input("enter your initial balance:"))
        
        while True:
            print("1. saving account")
            print("2. current account")
            choice=int(input("enter your choice: "))
            if choice==1:
                print("your account type is saving account")
            else:
                print("your account type is current account")
            break
        
        b1.openaccount(cname,acno,balance)
    elif choice==2:
        amount=int(input("enter deposite amount:"))
        b1.deposite(amount)
    elif choice==3:
        amount=int(input("enter withdraw amount:"))
        b1.withdraw(amount)
    elif choice==4:
        b1.checkbalance()
    elif choice==5:
        break
    else:
        print("invalid option")



