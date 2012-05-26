#!/usr/bin/python

###############################################################################
#
# Project Euler Problem 12
# found online at projecteuler.net/problem=12
#
###############################################################################

import math

target = 500
description = \
'The sequence of triangle numbers is generated by adding the natural\n' + \
'numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7\n' + \
' = 28. The first ten terms would be:\n\n' + \
'\t1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...\n\n' + \
'Let us list the factors of the first seven triangle numbers:\n\n' + \
'\t 1: 1\n' + \
'\t 3: 1,3\n' + \
'\t 6: 1,2,3,6\n' + \
'\t10: 1,2,5,10\n' + \
'\t15: 1,3,5,15\n' + \
'\t21: 1,3,7,21\n' + \
'\t28: 1,2,4,7,14,28\n\n' + \
'We can see that 28 is the first triangle number to have over five\n' + \
'divisors.\n\n' + \
'What is the value of the first triangle number to have over five\n' + \
'hundred divisors?\n'

def display(self):
    return description

###############################################################################
#
# Key realization:
# As sums of natural numbers, triangle numbers are all of the form 
# t = n*(n+1)/2.  Because n and n+1 are coprime, we can break down the
# number # of divisors by breaking the problem into D(n/2) and D(n+1) or 
# D(n) and D((n+1)/2), if D(n) computes the number of divisors of n
#
################################################################################

def numDivisors(n):
    if n & 1:	# n is odd
	return _numDivisors(n) * _numDivisors((n+1)/2)
    else:
	return _numDivisors(n/2) * _numDivisors(n+1)

def _numDivisors(x):
    count = 0
    for i in range (1,int(math.sqrt(x))):
 	if x % i == 0:
	    count += 1
    return count * 2

def solve(self):
    triangle = 1
    while numDivisors(triangle) < target:
        triangle += 1

    return triangle * (triangle+1) / 2


###############################################################################
# 
# If executed as a script/not imported
#
###############################################################################
if __name__ == '__main__':
    print solve(None)
