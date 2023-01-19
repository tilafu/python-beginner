#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0
    neg = 0
    zero = 0
    
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        elif i==0:
            zero += 1
    total = len(arr)
    
    positive_ratio = pos/total
    negative_ratio = neg/total
    zero_ratio = zero/total
    
    print(format(round(positive_ratio, 6)))
    print(format(round(negative_ratio, 6)))
    print(format(round(zero_ratio, 6)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
