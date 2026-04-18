while True:
    name = len(input("Write a name: "))
    if name <= 3:
        print("Invalid! The name must be at least 3 characters.")
    elif name > 50:
        print("Invalid! The name can have maximum of 50 characters.")
    else:
        print("That's a pretty good name!")
        break
