#!/usr/bin/python3

#This code simulates a simple ATM Withdrawal system

balance = 5000
amount = int(input("Enter amount to withdraw: "))

if amount % 100 != 0:
    print("Amount must be in multiples of 100")
elif amount + 10 > balance:
    print ("Insufficient balance")
else:
    balance -= (amount + 10) 
    print (f"Withdrawal successful. New balance: {balance}")
