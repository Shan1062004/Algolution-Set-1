def count_duplicates(arr):
    frequency = {}
    duplicates_count = 0
    
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    for count in frequency.values():
        if count > 1:
            duplicates_count += 1
    
    return duplicates_count

def main():
    numbers = []
    for _ in range(5):  
        num = int(input("Enter an integer: "))
        numbers.append(num)
    
    duplicates_count = count_duplicates(numbers)
    print("Total number of duplicate numbers:", duplicates_count)

main()
