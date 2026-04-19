list_of_books = ['Your Name', 'A Silent Voice', 'Demon Slayer', 'Suzume','Dandadan', 'Wind Breaker']
list_of_books_original_copy = list_of_books.copy()
# list_of_books.sort() 
list_of_books_borrowed = []


# count = len(list_of_books)
# numbers = [*range(1,count+1)] #list(range(1,count+1))  will work similarly
# for num, books in zip(numbers,list_of_books):
#     print(f'{num}. {books}')


print('Welcome to The Library System!')

while True:
    print('''HOMEPAGE
1. View Books available
2. Borrow a Book
3. Return a Book
4. Exit
''')

    try:
        option = int(input('Choose an option (1-4): '))
    except ValueError:
        print("Invalid Input! Words is not valid. Please select a number between 1 to 4.\n")
        continue

    if option == 1:
        if list_of_books:
            print('\nBooks available')
            for books in list_of_books:
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

            elif name_borrow.title().strip() in list_of_books:
                no = list_of_books.index(name_borrow.title().strip())
                print(f'You have successfully borrowed {list_of_books[no]}.\n')

                list_of_books_borrowed.append(list_of_books[no])
                list_of_books.remove(list_of_books[no])
                
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

            elif name_return.title().strip() in list_of_books_borrowed:
                no2 = list_of_books_borrowed.index(name_return.title().strip())
                print(f'You have successfully returned {list_of_books_borrowed[no2]}.\n')

                no3 = list_of_books_original_copy.index(list_of_books_borrowed[no2])   
                list_of_books.insert(no3,list_of_books_borrowed[no2])
                # list_of_books.append(list_of_books_borrowed[no2])
                # list_of_books.sort()
                list_of_books_borrowed.remove(list_of_books_borrowed[no2])
            
            else:
                print("Sorry, You may have mistyped. Try again!\nOr the book you want to return, doesn't belong to this Library System!\n")
                continue

            print('Enter 0 to Go Back.')
            print('Or If you have another book to return, go ahead.\n')
                
    elif option == 4:
        print('Thank you for using The Library System!\nSee you again soon!\nTake care!')
        break

    else:
        print("Invalid Input! Please select a number between 1 to 4.\n")
            
    
    
