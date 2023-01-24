def diagonalDifference(a):
    # Write your code here
    sum1 = 0
    sum2 = 0
    for i in range(len(a)):
        sum1 += a[i][i]
        sum2 += a[i][len(a)-1-i]
    return abs(sum1-sum2)

print(diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))