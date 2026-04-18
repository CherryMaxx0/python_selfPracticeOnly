
for numbers in range(1,21):
    if numbers % 5 ==0 and numbers % 3 == 0:
         print('fizzbuzz')
    elif numbers % 3 == 0:  #remember about the percentage system,, that i forgot while programming this
            print('fizz')
    elif numbers % 5 == 0:
         print('buzz')
    else:
        print(numbers)
    
