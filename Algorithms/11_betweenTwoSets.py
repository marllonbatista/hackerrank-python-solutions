#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    cont1=0
    cont2=0
    for j in range (max(a),min(b)+1):
        
        for x in a:
            if j%x == 0:
                cont1 +=1
        if cont1 == len(a):
            for y in b:
                if y%j == 0:
                    cont1 +=1        
        if cont1 == (len(a) + len(b)) :
            cont2 +=1
            
        cont1=0
        
    return cont2
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
