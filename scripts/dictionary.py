import hashlib

# Leaked pastebin of random accounts
# https://pastebin.com/Rdw5F4Qu

def dictionary():
    hash = input("Enter your hash: ")
    passwords = "../data/rockyou.txt"

    try:
        with open(passwords) as password:
            for line in password:
                line = line.strip()
                if hashlib.md5(line.encode('utf-8')).hexdigest() == hash:
                    print("The password is: %s" % line)
                    return ""
    except UnicodeDecodeError:
        print("Failed to crack the password.")

