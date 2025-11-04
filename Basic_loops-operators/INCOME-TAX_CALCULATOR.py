#!usr/bin/python3

#This program calculations the user's tax as per their income. A simple income tax calculator

print("Simple income tax calculator")

income = float(input("Enter your income: "))

if income <= 100000:
    tax_rate = 0
elif income <= 500000:
    tax_rate = 0.10
elif income <= 1000000:
    tax_rate = 0.20
else:
    tax_rate = 0.30

tax = income * tax_rate
net_income = income - tax

print(f"Tax Rate: {tax_rate * 100:.2f}%")
print(f"Tax to pay: {tax:.2f} KES")
print(f"Net income after tax: {net_income:.2f} KES")
