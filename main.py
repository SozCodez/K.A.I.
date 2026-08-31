#main python code file

import time 
import json
import os
import webbrowser
import urllib.parse
from urllib.parse import quote

#personalized users
kai = "K.A.I."

#age verif variable, false when started
adult = False

print("I'm K.A.I., your personal A.I. assistant! ")

time.sleep(1.5)


print("")
print("Who am I working with today? ")

usrName = input(":")


print("Age? ")
usrAge = input(":")

time.sleep(1)

#this logic changes users age from false to true if #over 18

if int(usrAge) >= 18: 
    adult = True

#personalized username kai


if usrName == "Kai":
    print()

    if adult:
        print("Welcome " + usrName + ". What can I do for you, creator? ")
        frstCmd = input(":")
#verif if adult
    if not adult:
        print()
        print("I'm sorry, I am restricted from minors. ")

#all other usr cept personalized

if usrName != "Kai":
    print()
#age verif
    if adult:
        print("Welcome " + usrName + ". What can I help you with? ")
        frstCmd = input(":")
    if not adult:
        print()
        print("I'm sorry, I am restricted from minors.")

#fst prompt results

if frstCmd == "nothing":
    print()
    time.sleep(1)
    print("Let me know when I can help.")

    frstCmd = input(":")


if frstCmd == "math":
    time.sleep(0.5)

    print()
    print("Whats our equation? ")
    mathQ = input(":")
    print()

    print("Calculating..")
    time.sleep(0.5)
    mathA = eval(mathQ)
    print(mathA)

#if prompt has no prededined result, websearch

if frstCmd != "math" and frstCmd != "nothing":
    query = frstCmd
    encoded_query = urllib.parse.quote(query)

    url = f"https://www.google.com/search?q={encoded_query}"

    print()
    print(f"Searching browser for: {query}")
    webbrowser.open(url)

#snd prompt results

print()
print("Anything else? ")
sndCmd = input(":")

if sndCmd == "nothing":
    print()
    time.sleep(1)
    print("Let me know when I can help.")

    sndCmd = input(":")


if sndCmd == "math":
    time.sleep(0.5)
    print()
    print("Whats our equation? ")
    mathQ = input(":")
    print()

    print("Calculating..")
    time.sleep(0.5)
    mathA = eval(mathQ)
    print(mathA)

if sndCmd != "math" and sndCmd != "nothing":
    query = sndCmd
    encoded_query = urllib.parse.quote(query)

    url = f"https://www.google.com/search?q={encoded_query}"

    print()
    print(f"Searching browser for: {query}")
    webbrowser.open(url)

time.sleep(1)

print()
print("Anything else? ")
trdCmd = input(":")

#trd prompt results

if trdCmd == "nothing":
    print()
    time.sleep(1)
    print("Let me know when I can help.")

    trdCmd = input(":")


if trdCmd == "math":
    time.sleep(0.5)
    print()
    print("Whats our equation? ")
    mathQ = input(":")
    print()

    print("Calculating..")
    time.sleep(0.5)
    mathA = eval(mathQ)
    print(mathA)

if trdCmd != "math" and sndCmd != "nothing":
    query = trdCmd
    encoded_query = urllib.parse.quote(query)

    url = f"https://www.google.com/search?q={encoded_query}"

    print()
    print(f"Searching browser for: {query}")
    webbrowser.open(url)

time.sleep(1)
print()
