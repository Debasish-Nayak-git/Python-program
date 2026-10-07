class Bank:
    name,ac="Ashu",25030521456
    def simple_interest(self,p,t,r):
        print("simple interset:",(p*t*r)/100)
class Account(Bank):
    balance=10000
    def operation(self):
        while 1:
            print("1.Deposite money")
            print("2.withdrow money")
            print("3.check balance")
            print("4.exit")
            ch=int(input("Enter your choice:"))
            if ch==1:
                rest=float(input("Enter amount to be deposited:"))
                if rest>0:
                    balance+=rest
                    print("Deposited successfully!")
                else:
                    print("Deposited amount must be positive")
            elif ch==2:
                rest=float(input("Enter amount to be withdraw:"))
                if rest<=10000:
                    balance-=rest
                    print("Withdrawed successfully!")
                else:
                    print("Insufficient Balance!")
            elif ch==3:
                print("Current Balance:",balance)
            elif ch==4:
                print("Thank you to use this ATM! Current balance=",balance)
                break
            else:
                print("Invalid choice")
class Saving_ac(Account):
    def ac_oper(self):
        print("Name:",sav.name,"\nAc no:",sav.ac)
        sav.operation()
sav=Saving_ac()
sav.ac_oper()
sav.simple_interest(sav.balance,12,7.8)