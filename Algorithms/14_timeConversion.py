#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    size=len(s)
    a= s[size -2:]
    time= s[:2]

    if a == 'PM':
        
        if time == '12':
            newTime=time
        else:
            newTime = str(int(time) + 12)
            
        newS=newTime + s[2:size-2]
    elif a == 'AM':
        if time == '12':
            time='00'
        newS = time + s[2:size-2]    
    
    return newS
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
