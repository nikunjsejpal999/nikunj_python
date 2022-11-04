class Bank:
    
    def openaccount(self,cname,type1,acno,balance):
        print("hello",cname,
              "your type of account is",type1,
              "and your account number is",acno,
              "with initial balance Rs.",balance)

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
cname=input("Enter customer name:")
type1=input("Enter your type of account:")
acno=int(input("enter account number:"))
balance=int(input("enter your initial balance:"))

b1.openaccount(cname,type1,acno,balance)

while True:
    print("1. deposite")
    print("2. withdraw")
    print("3. checkbalance")
    print("4. exit")

    choice=int(input("enter your choice: "))

    if choice==1:
        amount=int(input("enter deposite amount:"))
        b1.deposite(amount)
    elif choice==2:
        amount=int(input("enter withdraw amount:"))
        b1.withdraw(amount)
    elif choice==3:
        b1.checkbalance()
    elif choice==4:
        break
    else:
        print("invalid option")



