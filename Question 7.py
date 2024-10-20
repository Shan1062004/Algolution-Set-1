def print_unique_numbers(arr):
    unique_numbers = []
    for num in arr:
        if arr.count(num) == 1:
            unique_numbers.append(num)
    return unique_numbers

def main():
    numbers = []
    for _ in range(5): 
        num = int(input("Enter an integer: "))
        numbers.append(num)
    
    unique_numbers = print_unique_numbers(numbers)
    print("Unique numbers:", unique_numbers)

main()
