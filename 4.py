def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        minIdx = i

        for j in range (i+1,n):
            if arr[j] < arr[minIdx]:
                minIdx = j

        arr[i],arr[minIdx] = arr[minIdx],arr[i]
    
    return arr

arr=[64,54,45,23,10]
sorted_arr = selection_sort(arr)
print(sorted_arr)