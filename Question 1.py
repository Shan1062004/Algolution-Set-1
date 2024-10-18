def count_negativenum(arr):
    count=0
    for num in arr:
        if num < 0:
            count += 1 
    return count 
arr =[23,44,-23,4,-32]
print(count_negativenum(arr))