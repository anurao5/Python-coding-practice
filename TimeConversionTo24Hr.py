#!/bin/python3

import sys

def timeConversion(s):
    hr, mm, ss1 = s.split(':')
    ss = ss1[:2]
    ampm = ss1[2:]
    if hr == '12':
        if ampm == 'AM':
            hr = '00'
        else:
            hr = '12'
    else:
        if ampm == 'PM':
            hr = str(int(hr) + 12)
    return hr + ':' + mm + ':' + ss


s = input().strip()
result = timeConversion(s)
print(result)
