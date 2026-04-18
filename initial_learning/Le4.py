numbers = [2, 4, 1, 6, 45, 3, 34, 12, 23, 65, 7, 9, 10]
maximum = numbers[0]
for number_count in numbers:
    if maximum < number_count:
        maximum = number_count
print(maximum)

numbers2 = numbers.copy()
numbers.append(25)
print(numbers2)
    