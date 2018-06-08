import hashlib

hash = input("Enter your hash: ")
passwords = "../data/rockyou.txt"


def main():

    with open(passwords) as password:
        for line in password:
            line = line.strip()
            if hashlib.md5(line.encode('utf-8')).hexdigest() == hash:
                print("The password is: %s" % line)
                return ""
    print("Failed to crack the file.")


main()

