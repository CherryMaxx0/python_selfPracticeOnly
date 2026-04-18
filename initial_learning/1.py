def Data_Profile(name, age, gender, rank, y_n):
    print(f"Newly Joined Member info below:")
    print(f"Full Name: {name}")
    print(f"Age:", age, "Years old")
    print(f"Gender:", gender)
    print(f"Default Rank:", rank)
    experience = y_n
    if experience == True:
        print("Experience: Yes")
    elif experience == False:
        print("Experience: No")

Data_Profile("Kanao Tsuyuri", 16, "Female", "Hinoto", True)


