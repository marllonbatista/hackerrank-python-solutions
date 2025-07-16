#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    lowestValue  = min(arr)
    greaterValue = max(arr)
    arraySum = sum(arr)
    miniSun = arraySum - greaterValue
    maxSun= arraySum - lowestValue
    
    print(miniSun , maxSun)

    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
