import hashlib

hash_to_crack = input("Enter your hash: ")
dict_file = "../data/rockyou.txt"

def main():

    with open(dict_file) as fileobj:
        for line in fileobj:
            line = line.strip()
            if hashlib.md5(line.encode('utf-8')).hexdigest() == hash_to_crack:
                print("The password is: %s" % (line))
                return ""
    print("Failed to crack the file.")

if __name__ == "__main__":
    main()
