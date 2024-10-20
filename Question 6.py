def search_number(arr, target):
    if target in arr:
        return arr.index(target)
    else:
        return -1

def main():
    numbers = []
    for _ in range(5):  # You can adjust the range for a different array size
        num = int(input("Enter an integer: "))
        numbers.append(num)
    
    target = int(input("Enter the number to search for: "))
    index = search_number(numbers, target)
    
    print(index)

main()
