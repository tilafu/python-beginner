def count_occurrences(arr):
    count_dict = {}
    # range_arr from (0, 100)
    range_arr = range(100)

    #if the number is in the array, add it to the dictionary with the number of times it appears in the array
    for num in range_arr:
        if num in arr:
            count_dict[num] = arr.count(num)
        else:
            count_dict[num] = 0
  
    #create an array of the values of the dictionary
    arr2 = []
    for key, value in count_dict.items():
        arr2.append(value)
        
    return arr2

print(count_occurrences([1, 2, 3, 1, 2, 3, 4, 5, 4, 5, 4, 5]))
