def diagonalDifference(a):
    
    sum1 = 0
    sum2 = 0
    for i in range(len(a)):
        sum1 += a[i][i]
        sum2 += a[i][len(a)-1-i]
    return abs(sum1-sum2)

# The len(a)-1-i part of the code is what counts from the right. len(a) returns the number of rows in the 2D list a. Subtracting 1 from this value gives you the index of the last row.
# Subtracting i from this value gives you the index of the ith column counting from the right.

# For example, if a is a 5x5 list, len(a) would be 5 and len(a)-1 would be 4, which is the index of the last column. 
# If i is 3, then len(a)-1-i would be 4-1-3 = 0, which is the index of the first column counting from the right. 
# So this line of code is accessing the element at the 3rd row and the 1st column counting from the right of the 2D list a

# test
print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))