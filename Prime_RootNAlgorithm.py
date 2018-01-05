import sys
import math


def checkPrime(inp):

    for num in inp:
        if num == 1:
            prime = False
        elif num == 2:
            prime = True
        else:
            sq = int(math.sqrt(num))
            for i in range(2, sq+1):
                if num%i == 0:
                    prime = False
                    break;
                else:
                    prime = True
        if prime:
            print("Prime")
        else:
            print("Not prime")

count = int(input())
input_arr = []
for i in range(count):
    num = int(input())
    input_arr.append(num)

checkPrime(input_arr)



