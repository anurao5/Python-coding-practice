#!/bin/python3

import sys

#Minimum time to visit the list of homes in the given streets
def minimumTime(x):
    x.sort()
    min_dist = 0
    for i in range(1, len(x)):
        min_dist = min_dist + (abs(x[i] - x[i-1]))
    return min_dist


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        x = list(map(int, input().strip().split(' ')))
        result = minimumTime(x)
        print(result)
