import sys
from scripts.webscraper import scraper
from scripts.dictionary import dictionary
from scripts.sendMail import sendMail
from scripts.portScan import scanner

print("-------------------------------")
print("Welcome to the ultimate hacking")
print("/ reconnaissance tool!")
print("-------------------------------")

def recursiveCall():
    printMenu()

def printMenu():
    print("What do you want to do?")
    print("1) Scrape a website for E-mails")
    print("2) Scan a website for open ports (use localhost for test of your own machine)")
    print("3) Send \"Phishing E-mails\" to E-mails gathered from the webscraper")
    print("4) Launch a dictionary attack against a password hash")
    print("\n0) Exit the program")

    operation = input(">> ")

    if operation == "1":
        # webscraper
        scraper()

    elif operation == "2":
        # portscan
        scanner()

    elif operation == "3":
        # send mail
        sendMail()

    elif operation == "4":
        # dict attack
        dictionary()

    elif operation == "0":
        sys.exit("Program stopped by user")

    else:
        print("No menu entry with value: ", operation)
        print("Try one of the listed menu options.")
        print("\n\n\n\n")
        recursiveCall()

