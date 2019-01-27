#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 10:34:24 2019

@author: vpapg
"""
from Ch01_R import is_even
from random import shuffle, randint


def reverse_list(l):
    return [l[i] for i in range(len(l)-1,-1,-1)]

l = [1,5,2,3,4]
print(reverse_list(l))
print(list(reversed(l)))
print(l[::-1])
l.reverse()
print(l)
print()



def find_odd_product(l):
    odd_list=[]
    for element in l:
        if not is_even(element):
            odd_list.append(element)
    odd_list = list(set(odd_list))
    if len(odd_list)>=2:
        return (odd_list[0], odd_list[1], odd_list[0]*odd_list[1])
    else:
        return None

print(find_odd_product([1,2,3,4,5]))
print()



def are_distinct(l):
    check = list(set(l))
    if len(check) == len(l):
        return True
    else:
        return False

print(are_distinct([1,2,3,4]))
print(are_distinct([1,2,3,4,2]))
print()




print([k*(k+1) for k in range(10)])
print()



a = ord('a')
z = ord('z')
alphabet = [chr(letter) for letter in range(a,z+1)]
print(alphabet)
print()



def shuffler(l):
    shuffled = [None] * len(l)
    for element in l:
        idx = randint(0,len(l)-1)
        while shuffled[idx] is not None:
            idx = randint(0,len(l)-1)
        shuffled[idx] = element
    return shuffled

print(shuffler([10,20,30,40]))
print()



