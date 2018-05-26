#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getWays function below.
def getWays(n, c, memo):
    #if n is 0, then the combination of elements used is valid and hence will count towards the number of ways
    if n ==0:
        return 1
    #if n is less than 0, then the combination of elements used is not valid and will not count towards the ways
    elif n < 0:
        return 0
    #c[1:0] for list of one element will return an empty list and no possible ways from this combination
    elif len(c)==0:
        return 0
    
    #Create a cache with key uniquely represting the n and list c
    key = (tuple(c),n)
    if key in memo:
        return memo[key]
    else:
        output = (getWays(n-c[0],c,memo) + getWays(n,c[1:],memo))
        memo[key] = output
        return output

if __name__ == '__main__':

    nm = input().split()
    n,m = int(nm[0]),int(nm[1])
    c = list(map(int, input().rstrip().split()))
    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    
    memo = {}
    ways = getWays(n, c , memo)
    
    print(ways)