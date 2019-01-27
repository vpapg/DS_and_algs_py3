#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 00:23:49 2019

@author: vpapg
"""

from random import randrange

def is_multiple(n,m):
    if n%m==0:
        return True
    else:
        return False

def is_even(k):
    evenlist = ['0','2','4','6','8']
    if str(k)[-1] in evenlist:
        return True
    else:
        return False

def minmax(data):
    minnum = 0
    maxnum = 0
    for num in data:
        if num<minnum:
            minnum=num
        elif num>maxnum:
            maxnum=num
    return (minnum,maxnum)

def sum_of_squares(n):
    s = 0
    for num in range(0,n):
        s += num**2
    ss = sum([num**2 for num in range(0,n)])
    return (s,ss)

def sum_of_squares_odd(n):
    s = 0
    for num in range(0,n):
        if not is_even(num):
            s += num**2
    ss = sum([num**2 for num in range(0,n) if not is_even(num)])
    return (s,ss)

def negative_index(string,k):
    idx = len(string)+k
    print(idx, string[k], string[idx])

def range_constructor01():
    for num in range(50,90,10):
        print(num)

def range_constructor02():
    for num in range(8,-10,-2):
        print(num)
        
def list_2powers():
    return [2**num for num in range(9)]


def return_choice(data):
    return randrange(data[0], data[-1])

print(is_multiple(10,5),is_multiple(6,2),is_multiple(10,3))
print(is_even(10),is_even(394875),is_even(102093484))
print(minmax([1,0,-7,32,586,4]))
print(sum_of_squares(4))
print(sum_of_squares_odd(4))
negative_index("goodbye",-3)
print()
range_constructor01()
print()
range_constructor02()
print()
print(list_2powers())
print(return_choice([1,5,7,9,2,6]))