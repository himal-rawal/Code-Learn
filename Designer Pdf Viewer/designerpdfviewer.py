#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    tallest=[]
    alphabet_list = list(string.ascii_lowercase)
    dict_from_list = dict(zip(alphabet_list, h))
    for i in range(len(word)):
        for key, value in dict_from_list.items():
            if key==word[i]:
                tallest.append(value)
    return max(tallest)*len(word)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
