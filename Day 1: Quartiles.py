#!/bin/python3
from statistics import median

n = int(input())
x = sorted(list(map(int, input().split())))
    
print(int(median(x[:n//2])))
print(int(median(x)))
print(int(median(x[(n+1)//2:])))
