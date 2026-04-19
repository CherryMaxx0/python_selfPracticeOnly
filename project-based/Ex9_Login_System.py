
import sys
sys.path.append(r"c:\CMX\CMX everything PC\EVERY - Projects CMX-PC\Coding\Python_learning\Hash_SHA256")
from SHA256_hash_tool import hash_text_sha256
# sys.path.append("..")
# from Hash_SHA256.SHA256_hash_tool import hash_text_sha256

# import hashlib


# from getpass import getpass  #this can't hide the character with a replacement
import msvcrt

def input_astericks(prompt=""):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = msvcrt.getch()
        if char in {b"\r", b"\n"}:  # Enter key
            print()
            break
        elif char == b"\x08":  # Backspace
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += char.decode("utf-8")
            print("*", end="", flush=True)
    # print(password)
    return password





# Example idea (not full code):
users = {}  # username: password
login_succes = False

while True:
    print("Homepage\n1. Login\n2. Don't have account? Register One Now!\n3. Exit")
    try:
        choice = int(input("Choose a No.: "))
    except ValueError:
        print("Invalid! You have to Choose only number. (1 or 2)\n")
        continue

    #Login-------------------------------
    if choice == 1:
        t0 = 8
        n0 = ''
        while t0 > 0: #username
            username_try = input("\nEnter username: ")
            if username_try in users:
                break

            else:
                t0 -= 1
                if t0 < 7 and t0 > 0:
                    print("Incorrect username!\nDon't have account? Enter '0' to go back, or enter anything to continue.")
                    n0 = input("Enter: ")
                    if n0 == '0':
                        break

                elif t0 == 7:
                    print("Incorrect username! Try again.\n")
                    continue
                else:    
                    print('You have entered incorrect username multiple times.\n')
                    break

        if n0 == '0':
            continue
        elif t0 == 0:
            continue
         
        t1 = 8
        n1 = ''
        while t1 > 0: #password
            password_try_hash =  hash_text_sha256(input_astericks("Enter password: "))  # direct convert to hash
            if password_try_hash == users[username_try]:
                login_succes = True
                print("Login Successfully!")
                break

            else:
                t1 -= 1
                if t1 < 5 and t1 > 0:
                    print("Incorrect password!\nDon't have account? Enter '0' to go back, or enter anything to continue.")
                    n1 = input("Enter: ")
                    if n1 == '0':
                        break
                    
                elif t1 >= 5:
                    print("Incorrect password! Try again.\n")
                    continue
                else:
                    print("You have entered incorrect password multiple times.\n")
                    break 
                
        if n1 == '0':
            continue
        elif t1 == 0:
            continue
        elif login_succes:
            break
    # Login -------------------------                         


    # Register----------------------------
    elif choice == 2: #Register
        while True:
            username = input("\nCreate username: ")
            if username in users:
                print("Sorry, the username is already taken. Try another!")
            else:
                break
            
        pass_hash256 = hash_text_sha256(input_astericks("Create password: "))
        #idk but without using variable to save the input to convert, instead directly converting the pass to hash feels safer
        users[username] = pass_hash256                              
        # print(users)
        print(pass_hash256)
        print('User ID Registered Successfully!\n')
    # Register----------------------------

    elif choice == 3:
        print("Exited the System")
        break

    else:
        print('Invalid! Choose 1 or 2.\n')

