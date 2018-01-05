#!/bin/python3

import sys
import re
import operator

N = int(input().strip())
namelist = []

#Display names who have a gmail ID in alphabetical order
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.match(r'[\w.-]+@gmail\.com$', emailID):
        namelist.append(firstName)

print(*sorted(namelist), sep='\n')
