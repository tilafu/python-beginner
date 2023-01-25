#function that prints the maximum and minimum sums of an array of numbers
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
