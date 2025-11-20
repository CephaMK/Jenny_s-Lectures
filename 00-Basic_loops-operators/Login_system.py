#!usr/bin/python3

#This program simulates a simple case sensitive login system

username = "Mwangi"
password = "PythonRocks123"

user = input("Username: ")
pwd = input ("Password: ")

if user.upper() == username.upper() and pwd == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
