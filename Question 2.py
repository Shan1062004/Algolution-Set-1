def max_of_five():
    numbers = []
    for i in range(5):
        num = int(input("Enter Integers"))
        numbers.append(num)
    max_num = max(numbers)
    print("The Maximum Number is:",max_num)
max_of_five()