#function that sorts an array of numbers from smallest to largest
def minMax(array):
    #sorts the array
    array.sort()
    #add the first n-2 numbers
    minSum = sum(array[:len(array)-1])

    #reverse 
    array.reverse()
    maxSum = sum(array[:len(array)-1])
    print(f"{minSum} {maxSum}")

#array of numbers
array = [3,2,1,4,5]
minMax(array)
