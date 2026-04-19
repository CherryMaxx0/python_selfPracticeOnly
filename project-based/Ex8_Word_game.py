import random

#Word Lists for difficulty
animal = ['dog', 'cat', 'lion', 'tiger', 'elephant', 'monkey', 'zebra', 'giraffe', 'rabbit', 'fox', 'bear', 'wolf', 'panda', 'horse', 'goat', 'deer', 'rat', 'mouse', 'snake', 'frog']


difficult_words = ['astronomy', 'galaxy', 'crimson', 'mystify', 'vortex', 'symphony', 'cascade', 'phantom', 'labyrinth', 'enigmatic','zephyr', 'paradox', 'alchemy', 'serendipity', 'eclipse', 'dusk', 'ember', 'voyage', 'euphoria', 'whisper','nebula', 'mirage', 'onyx', 'horizon', 'tapestry', 'cipher', 'spectrum', 'solstice', 'luminous', 'ravenous']


#Main Game Below

# random_word = random.choice(animal)

print('\nWelcome to the Word Guessing Game.')
while True:
    diff = input("Choose, Easy(E/e) or Hard(H/h): ").lower().strip()
    if diff in ['easy','e','hard','h']:
        break
    else:
        print("Invalid input! Please enter 'Easy' or 'Hard', and in exact spelling\n")
    
if diff == 'hard' or diff == 'h':
    random_word = random.choice(difficult_words)
elif diff == 'easy' or diff == 'e':
    random_word = random.choice(animal)
    print('Hint: Animal')

# print(f'\n{len(random_word)} and {random_word}')

guessed_letter = []
chances = 10
print(f"\n\nYou have {chances} chances.")

while 0 < chances:
    # print(guessed_letter)
    display_word = ''
    for letter in random_word:
        if letter in guessed_letter:
            display_word += letter
        
        else:
            display_word += ' _ '


    print(f'\n\nWord: {display_word}')    

    if display_word == random_word:
        print("OH! Actually Congrats!! You Got it! That's the word")
        break        

    guessed = input('Give your guess (a letter or the whole word): ').lower().strip()
    
    if guessed == random_word:
        print("OMG! You are Genius!! Lucky or not! But that's Perfect Guess, all in one go.")
        break

    elif guessed in display_word:
        print(f'There are no more "{guessed}" in this word.')
        continue

    elif guessed in guessed_letter:
        print(f'You have guessed "{guessed}" already.')
        continue
    
    elif guessed not in random_word:
        if len(guessed) == 1:
            print(f"No '{guessed}' is in this Word.")
            guessed_letter.append(guessed)

    elif guessed in random_word:
        if len(guessed) == 1:
            guessed_letter.append(guessed)
            print("Nice guess! Keep going.")
        else:    
            for let in guessed:
                guessed_letter.append(let)
            print("WOW! That's Wild!! Guess the rest!")
        continue

        #This is to deduct point, using else doesn't deduct at all.

    if guessed not in random_word or guessed != random_word:
        chances -= 1
        print(f"It's a Wrong Guess! Chances left: {chances}")
        if chances == 0:
            print(f'\nGAME OVER!! You ran out of your chances!\nThe correct word is {random_word}')
            break

print("\nSee you Next Time!")
