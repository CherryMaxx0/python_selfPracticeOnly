Emojis = {':)': '🙂',
          ':(': '🙁',
          ';P': '😜',
          ';)': '😉',
          ':/': '😕',
          'XD':'😆',
          ':O': '😮',
          '-_-': '😑'
}
message = input("Send a Message: ")
words = message.split(' ')
Output = ""
for word in words:
    Output += Emojis.get(word, word) + " "
print(Output)

