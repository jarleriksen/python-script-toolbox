

print("-------------------------------")
print("Welcome to the ultimate hacking")
print("/ reconnaissance tool!")
print("-------------------------------")


def printMenu():
    print("What do you want to do?")

    operation = input(">> ")

    if operation == "1":
        # webscraper
        pass

    elif operation == "2":
        # portscan
        pass

    elif operation == "3":
        # send mail
        pass

    elif operation == "4":
        # dict attack
        pass

    else:
        print("No menu entry with value: ", operation)
        print("Try one of the listed menu options.")
