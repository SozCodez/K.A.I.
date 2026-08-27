#main python code file

import time 
import json
import os


kai = "K.A.I."
adult = False

print("I'm K.A.I., your personal A.I. assistant! ")

time.sleep(1.5)


print("")
print("Who am I working with today? ")

usrName = input(":")


print("Age? ")
usrAge = input(":")

time.sleep(1)

if int(usrAge) >= 18: 
    adult = True

if usrName == "Kai":
    print()

    if adult:
        print("Welcome " + usrName + ". What can I do for you, creator? ")
        frstCmd = input(":")
    if not adult:
        print()
        print("I'm sorry, I am restricted from minors. ")

if usrName != "Kai":
    print()

    if adult:
        print("Welcome " + usrName + ". What can I help you with? ")
        frstCmd = input(": ")
    if not adult:
        print()
        print("I'm sorry, I am restricted from minors.")


if frstCmd == "nothing":
    print()
    time.sleep(1)
    print("Let me know when I can help.")

if frstCmd == "math":
    print()
    print("Whats our equation? ")
    mathQ = int(input(""))
    
