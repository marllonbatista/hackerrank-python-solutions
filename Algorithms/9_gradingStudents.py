#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    gradesOut=[]
    for x in grades:
        for i in range(0,101,5):
            if x < 38:
                gradesOut.append(x)
                break
            elif x == 100:
                gradesOut.append(x)
                break
            elif x < i :
                subtraction = i - x 
                if subtraction < 3:
                    gradesOut.append(i)
                else:
                    gradesOut.append(x)
                break
    
    return gradesOut
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
