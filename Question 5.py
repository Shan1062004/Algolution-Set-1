def is_palindrome_array(arr):
    return arr == arr[::-1]

def check_palindrome():
    numbers = []
    for _ in range(5):
        num = int(input("Enter an integer: "))
        numbers.append(num)
    
    if is_palindrome_array(numbers):
        print("The array is in palindrome order.")
    else:
        print("The array is not in palindrome order.")

check_palindrome()
