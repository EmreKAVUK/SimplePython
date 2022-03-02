import hashlib
from termcolor import colored
def md5():
    print(colored("             MD5              ", "blue"))
    hash = hashlib.md5()
    hash.update(text.encode())
    print(colored(hash.hexdigest(), "red"))

def sha256():
    print(colored("            SHA256              ", "blue"))
    hash = hashlib.sha256()
    hash.update(text.encode())
    print(colored(hash.hexdigest(), "green"))

def sha512():
    print(colored("            SHA512            ", "blue"))
    hash = hashlib.sha512()
    hash.update(text.encode())
    print(colored(hash.hexdigest(), "green"))


value = True
while value:
    print("""
    1-) MD5
    2-) SHA256
    3-) SHA512
    4-) EXIT
    """)
    a = int(input("Select one"))
    if(a == 1):
        text = input("Enter your input \n")
        md5()
    elif(a == 2):
        text = input("Enter your input \n")
        sha256()
    elif(a == 3):
        text = input("Enter your input \n")
        sha512()
    elif(a ==4):
        print("Exiting the application")
        value = False
    else:
        print("Please enter 1-4")






