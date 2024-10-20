def count_frequencies(arr):
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency

def main():
    numbers = []
    for _ in range(5):  
        num = int(input("Enter an integer: "))
        numbers.append(num)
    
    frequencies = count_frequencies(numbers)
    print("Frequencies of each number:", frequencies)

main()
