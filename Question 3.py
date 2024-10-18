def merged_sorted_arrays(arr1,arr2):
    i,j = 0,0
    merged_array =[]
    while i < len(arr1) and j < len(arr2):
        if arr1[i]<arr2[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
        
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    
    return merged_array

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
Merged =merged_sorted_arrays(arr1,arr2)
print("Merged Sorted arrays",Merged)