


def palindrome(word_input):
    word = word_input.lower()
    reverse_word = ''.join(reversed(word))
    reverse_word1 = ''.join(reversed(word_input))
    phrase = ''.join(word.split())

    if reverse_word == word:
        print(f'''
The Original Word you entered in reversed: {reverse_word1}
In caps: {reverse_word.upper()} and In Lowercase: {reverse_word}
''')
        print("So, Yess, it's a palindrome!")
    elif phrase == phrase[::-1]: #this is different way to reverse the wordings/letters
        print("Yeah, it's a palindrome phrase!")

    else:
        print("Therefore, Nope, it's not a palindrome.")

if __name__ == "__main__":
    palindrome(input("Enter the word: "))

