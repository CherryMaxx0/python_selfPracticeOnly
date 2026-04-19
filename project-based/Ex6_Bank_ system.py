print('''Welcome to Simple Bank System!
HOMEPAGE
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Exit
''')

balance = 0
while True:
    try:
        option = int(input('Choose an option (1-4): '))
    except ValueError:
        print("""Invalid Input! Words is not valid. Please select a number between 1 to 4.
               """)
        continue

    if option == 1:
        print(f'''Your Bank Balance is: ${balance}
''')

    elif option == 2:
        while True:
            print('Enter $0, to go back')
            try:
                amount_depo = int(input('Enter the amount to deposit: $'))
            except ValueError:
                print("""Invalid Input! Words is not valid. Please use values to deposit the amount.
               """)
                continue

            if amount_depo == 0:
                print('Returned back to HOMEPAGE')
                break
            elif amount_depo > 0:
                balance += amount_depo
                print(f'''${amount_depo} deposited successfully!
                    ''')
                break
            else:
                print("""Invalid! Negative input can't be used!
                      """)
                
#Line25 to Line30: Instead of this Try-Except function to handle Error input                
            # else:
            #     print("""Error Input! I can't take words as input.
            #   """)
                
    elif option == 3:
        while True:
            print('Enter $0, to go back')
            try:
                amount_withdr = int(input('Enter the amount to withdraw: $'))
            except ValueError:
                print("""Invalid Input! Words is not valid. Please use values to withdraw the amount.
               """)
                continue

            if amount_withdr == 0:
                print('Returned back to HOMEPAGE')
                break

            #Maintain Order always. First need to check the balance then withdrawal process.
            elif balance < amount_withdr:
                    print('''Sorry, cannot be withdrawn due to insufficient balance in your account.
                          ''')
            elif amount_withdr > 0:
                balance -= amount_withdr
                print(f'''${amount_withdr} withdrawn successfully!
                        ''')
                break

            else:
                print("""Invalid! Negative input can't be used!
                      """)
                
#Line52 to Line57: Instead of this Try-Except function to handle Error input                
            # else:
            #     print("""Error Input! I can't take words as input.
            #   """)

    elif option == 4:
        print('Thank you for using The Simple Bank system!')
        break

    else:
        print("""Invalid Choice! Please select a number between 1 to 4.
              """)
        
#Line11 to Line16: Instead of this Try-Except function to handle Error input
    # else:
    #     print("""Error Input! I can't take words as input.
    #           """)