def reverse_array():
    numbers = []
    for i in range(7):
        num = int(input("Enter an integer: "))
        numbers.append(num)
    
    reversed_numbers = numbers[::-1]
    
    print("Reversed numbers:", reversed_numbers)
reverse_array()
