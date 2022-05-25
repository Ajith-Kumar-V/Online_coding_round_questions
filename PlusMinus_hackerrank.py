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
    arr=arr
    n=0
    z=0
    p=0
    l=len(arr)
    for i in arr:
        if i==0:
            z=z+1
        elif i<0:
            n=n+1
        elif i>0:
            p=p+1
    print(p/l)
    print(n/l)
    print(z/l)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
