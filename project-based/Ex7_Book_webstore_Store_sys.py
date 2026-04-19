import json
import sys

file_path = "hokako/Storage/Book_Store.json"

#List of the initial books data structure
list_of_books = ['Your Name', 'A Silent Voice', 'Demon Slayer', 'Suzume','Dandadan', 'Wind Breaker']
list_of_books.sort()
list_of_books_borrowed = []

#Data dictionary for json storage, to modify
data = {
    "list_books": list_of_books,
    "list_books_borrowed": list_of_books_borrowed
}


try:
    with open(file_path, 'x') as file:
        json.dump(data, file, indent=4)
        # print("Done")
except FileExistsError:
    pass


try:
    with open(file_path, "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("Data file not found, can't continue to proceed further!")
    sys.exit()
except PermissionError:
    print("System don't have persmission to access the data file, can't proceed further!")
    sys.exit()
    

print('Welcome to The Library System!')
while True:

    currently_available = data["list_books"]
    currently_borrowed = data["list_books_borrowed"]

    print("HOMEPAGE\n1. View Books available\n2. Borrow a Book\n3. Return a Book\n4. Exit")

    try:
        option = int(input('Choose an option (1-4): '))
    except ValueError:
        print("Invalid Input! Words is not valid. Please select a number between 1 to 4.\n")
        continue

    if option == 1:
        if currently_available:
            print('\nBooks currently available are:')
            for books in currently_available:
                print(f'- {books}')
        else:
            print('\nNo Books is currently avalaible')

        while True:
            try:
                num = int(input('\nEnter 0 to Go Back: '))
            except ValueError:
                print("Invalid Input! Please enter 0 (zero), to Go Back HOMEPAGE.\n")
                continue
                
            if num == 0:
                print('Returned to HOMEPAGE\n')
                break
            else:
                print("Invalid Input! Please enter 0 (zero), to Go Back HOMEPAGE.")
                
    elif option == 2: 
        print('\nEnter 0 to Go Back.')
        while True:
            name_borrow = input('Enter the name of the Book tor Borrow: ')   

            if name_borrow == '0':
                print('Returned to HOMEPAGE\n')
                break

            elif name_borrow.title().strip() in currently_available:
                no = currently_available.index(name_borrow.title().strip())
                print(f'You have successfully borrowed {currently_available[no]}.\n')

                currently_borrowed.append(currently_available[no]) 
                currently_available.remove(currently_available[no])
                
            else:
                print("Sorry, You may have mistyped. Try again!\nOr the book you want to borrow is currently unavailable!\n")
                continue  #continue is use to go back to the start of the while loop, does not matter what's under!!

            print('Enter 0 to Go Back.')
            print('Or If you want to Borrow another book, go ahead.\n')
            
    elif option == 3:
        print('\nEnter 0 to Go Back.')
        while True:
            name_return = input('Enter the name of the Book to Return: ')

            if name_return == '0':
                print('Returned to HOMEPAGE\n')
                break

            elif name_return.title().strip() in currently_borrowed:
                no2 = currently_borrowed.index(name_return.title().strip())
                print(f'You have successfully returned {currently_borrowed[no2]}.\n')

                # no3 = list_of_books_original_copy.index(list_of_books_borrowed[no2])   
                # list_of_books.insert(no3,list_of_books_borrowed[no2])
                currently_available.append(currently_borrowed[no2])
                currently_available.sort()
                currently_borrowed.remove(currently_borrowed[no2])
            
            else:
                print("Sorry, You may have mistyped. Try again!\nOr the book you want to return, doesn't belong to this Library System!\n")
                continue

            print('Enter 0 to Go Back.')
            print('Or If you have another book to return, go ahead.\n')
                
    elif option == 4:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print('Thank you for using The Library System!\nSee you again soon!\nTake care!')
        break

    else:
        print("Invalid Input! Please select a number between 1 to 4.\n")
            
    
    
