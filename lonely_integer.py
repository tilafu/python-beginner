def lonelyInteger(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i

arr=[1,1,2,2,3,3,4,5,5,6,6,7,7,8,8]
print(lonelyInteger(arr))