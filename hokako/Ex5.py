secret_number = 47
guess_count = 0
print('A secret number between 1 to 100 is been chosen.')
while True:
    guess = int(input('Guess the number: '))
    guess_count += 1
    if guess == secret_number:
        if guess_count == 1:
            print(f'Yout got it!! You guessed it in {guess_count} attempt.')
        else:
            print(f'Yout got it!! You guessed it in {guess_count} attempts.')
        break
    if guess > secret_number:
        print('Too high!')
    if guess < secret_number:
        print('Too Low!')
    print(f'No. of Attempts: {guess_count}')


