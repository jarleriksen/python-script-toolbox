import sys

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
        print("webscraper call here")
        # webscraper
        pass

    elif operation == "2":
        print("portscan call here")
        # portscan
        pass

    elif operation == "3":
        print("send mail call here")
        # send mail
        pass

    elif operation == "4":
        print("dict attack call here")
        # dict attack
        pass

    elif operation == "0":
        sys.exit("Program stopped by user")

    else:
        print("No menu entry with value: ", operation)
        print("Try one of the listed menu options.")
        print("\n\n\n\n")
        recursiveCall()

