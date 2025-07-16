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
    
    contPositive=0
    contNegative =0
    contZero=0
    
    arraySize = len(arr)
    for i in arr:
        if i > 0:
            contPositive= contPositive + 1
        elif i < 0:
            contNegative= contNegative+1
        else :
            contZero=contZero+1
    print(contPositive/arraySize)
    print(contNegative/arraySize)
    print(contZero/arraySize)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
