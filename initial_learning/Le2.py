started = False
while True:
    command = input('> ').lower()
    if command == "start":
        if started: #if true then it is printed
            print("Car is already started.")
        else: #since not true, else is printed
            started = True  #also setting the started to True
            print("Car started... ")

    elif command == "stop":
        if not started:  #if started is false then it is printed
            print("Car is already stopped.")
        else:  #depends on the start input which changes the started to True, then it is printed
            started = False #sets the started to False
            print("Car stopped.")

    elif command == "help":
        print('''
Type Start - To start the car
Type Stop - To stop the car
Type quit - To Quit the game''')
        
    elif command == "quit":
        break

    else:
        print("Sorry, I don't understand that.")
        