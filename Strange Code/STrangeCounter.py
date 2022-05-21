#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter(t):
    # Write your code here
    value=3
    while True:
        t-=value #eg t=5 then t=5-3 , t=2
        if(t<=0): #check 2<=0  ans=false and than value=3*2=6 again 2-6=-4 
            t+=value #check -4<0 true then t=-4+6=2 than
            return value-t+1 #return 6-2+1=5
        value*=2
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
