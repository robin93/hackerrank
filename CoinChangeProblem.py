#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getWays function below.
def getWays(n, c, memo):
    if n ==0:
        return 1
    elif n < 0:
        return 0
    elif len(c)==0:
        return 0
    
    key = (tuple(c),n)
    if key in memo:
        return memo[key]
    else:
        output = (getWays(n-c[0],c,memo) + getWays(n,c[1:],memo))
        memo[key] = output
        return output

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    
    memo = {}
    ways = getWays(n, c , memo)
    
    print(ways)