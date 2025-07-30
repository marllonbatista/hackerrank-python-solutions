#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    
    arrayScores=[0,0]
    minimum=maximum=scores[0]
    for i in scores:
        if i > maximum:
            arrayScores[0] +=1
            maximum = i
        elif i < minimum:
            arrayScores[1] +=1 
            minimum = i
            
    return arrayScores
       
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
