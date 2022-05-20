#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#
def reverse(m):
    revs=0
    while(m>0):
        a = m % 10
        revs = revs * 10 + a
        m = m // 10
    #print("rev:",revs)
    return revs
        
def beautifulDays(i, j, k):
    # Write your code here
    count=0
    for l in range(i,j+1):
        rev=reverse(l)
        #print(rev)
        #print(l)
        h=l-rev
        #print(h)
        beautifulnumber=(abs(l-rev))/k
        #print(beautifulnumber)
        if(beautifulnumber-int(beautifulnumber)==0):
            count+=1
        rev=0
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
