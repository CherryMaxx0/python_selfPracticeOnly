def greet_user(given_name, surname_name):
    print(f'''
Hey,{surname_name} {given_name}''')
    print("Welcome to FashionJP Limited")
    print(f'''
How may i assist you Today? {surname_name}-sama''')


#print('Write your Full name below as')
#last_name = input("Surname: ")
#first_name = input("Given: ")
#greet_user(first_name, last_name)

print('Write your Full Name below as [Surname Given]')
name = input("Name: ")
namesplit = name.split(' ')
greet_user(namesplit[1], namesplit[0])
