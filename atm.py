import random

class atm(object):
    def __init__(self, ATMnumber, ATMpin):
        self.ATMnumber = ATMnumber
        self.ATMpin = ATMpin

    def cashWithdrawl(self, ATMnumber, ATMpin):
        amount = int(input("Enter the amount you want to withdraw: "))
        print("\nThe amount Rs. " + str(amount) + " has been withdrawn from Card number: " + str(ATMnumber) + " and pin: " + str(ATMpin) + "\n")

    def enquireBalance(self, ATMnumber, ATMpin):
        balance = random.randint(500, 10000)
        print("\nYou currently have Rs. " + str(balance) + " in Card number: " + str(ATMnumber) + " and pin: " + str(ATMpin) + "\n")

    def depositMoney(self, ATMnumber, ATMpin):
        depositAmount = int(input("Enter the amount you want to deposit: "))
        print("\nYou have successfully deposited Rs. " + str(depositAmount) + " in Card number: " + str(ATMnumber) + " and pin: " + str(ATMpin) + "\n")

    def takeALoan(self, ATMnumber, ATMpin):
        loanAmount = int(input("Enter the loan amount: "))
        print("\nYour loan of Rs. " + str(loanAmount) + " in Card number: " + str(ATMnumber) + " and pin: " + str(ATMpin) + " has been granted!\n")

    def payBill(self, ATMnumber, ATMpin):
        billAmount = random.randint(1000, 5000)
        print("\nYour bill of Rs. " + str(billAmount) + " through Card number: " + str(ATMnumber) + " and pin: " + str(ATMpin) + " has been paid!\n")

print("Choose your desired action:\n\nPress c for withdrawing cash\nPress e for balance enquiry\nPress d to deposit money\nPress l to take a loan\nPress p for paying a bill\n")
action = input("Enter your action: ")

ATM = atm(15, 20)
if action == "c":
    ATM.cashWithdrawl(int(input("Enter your Card Number: ")), int(input("Enter your Card Pin: ")))
elif action == "e":
    ATM.enquireBalance(int(input("Enter your Card Number: ")), int(input("Enter your Card Pin: ")))
elif action == "d":
    ATM.depositMoney(int(input("Enter your Card Number: ")), int(input("Enter your Card Pin: ")))
elif action == "l":
    ATM.takeALoan(int(input("Enter your Card Number: ")), int(input("Enter your Card Pin: ")))
elif action == "p":
    ATM.payBill(int(input("Enter your Card Number: ")), int(input("Enter your Card Pin: ")))