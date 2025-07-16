#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    
    arraySize=len(arr) - 1
    
    sumPrimaryDiagonal=0
    sumSecondaryDiagonal=0
    
    for i in range(len(arr)) :
        sumPrimaryDiagonal= arr[i][i] + sumPrimaryDiagonal
        j = arraySize - i
        sumSecondaryDiagonal = arr[i][j] + sumSecondaryDiagonal
    
    difference = abs(sumPrimaryDiagonal - sumSecondaryDiagonal)
    
    return difference
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
