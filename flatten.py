#   Created by Elias Muchai 
#   MIT license. Feel free to use & abuse ;-0

# flatten Solution
#

def flatten(listItems):
    results = []
    for item in listItems:
        if type(item) is list:
            results.extend(flatten(item))
        else:
            results.append(item)
    return(results)


print(flatten([1, 2, 3, [4, 5]])) # [1, 2, 3, 4, 5]
print(flatten([1, [2, [3, 4], [[5]]]])) # [1, 2, 3, 4, 5]
print(flatten([[1], [2], [3]])) # [1, 2, 3]
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) # [1, 2, 3]