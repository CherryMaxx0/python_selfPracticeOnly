number_to_letter1 = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J',
                   11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S',
                   20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'}
# Using integer is not a good choice, since you have to make it string anyway

number_to_letter = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I',
                   '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', 
                   '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', 
                   '25': 'Y', '26': 'Z'}


def conversion(code_no):
    code_splited_list = code_no.split(" ")
    output = ''
    for code_split in code_splited_list:
        output += number_to_letter.get(code_split,'[?:/]')
    print('Decoded message: ', output)
    if any(code_split not in number_to_letter for code_split in code_splited_list):
        print("Invalid! I can't distinguish the code. Put space between each code no. or you may be using code outside the valid range of 1-26.")
    
def pro_coversion():
    # Get user input
    code = input("Enter the secret code: ")

    # Split the input into a list of numbers
    numbers = code.split()

    # Convert each number to a letter
    message = ''.join(chr(int(num) + 64) for num in numbers)

    # Print the decoded message
    print("Decoded message:", message)



secret_code = input("Write the secret code: ")
conversion(secret_code)
