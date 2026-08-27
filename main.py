#main python code file

import time 

kai = "K.A.I."
adult = False


print("I'm K.A.I., your personal A.I. assistant! ")

time.sleep(1.5)


print("")
print("Who am I working with today? ")

usrName = input(":")

print("Age? ")
usrAge = input(":")

if int(usrAge) >= 18: 
    adult = True

print()

if adult:
    print("Welcome " + usrName + ". What can I do for you? ")
    frstCmd = input(":")

if not adult:
    print("I'm sorry, I am restricted from minors. ")


