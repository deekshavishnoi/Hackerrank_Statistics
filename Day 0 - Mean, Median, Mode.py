#!/bin/python3
import statistics
n= int(input())
arr = sorted(list(map(int, input().split())))

print(statistics.mean(arr))
print(statistics.median(arr))
print(statistics.mode(arr))