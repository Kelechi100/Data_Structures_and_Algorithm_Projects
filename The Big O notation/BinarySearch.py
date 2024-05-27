# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 11:03:16 2024

@author: s22ilogkele
"""

def binary_search(item_list, item):
    
    n=0
    first = 0
    last = len(item_list)-1
    found = False
     
    while first <= last and not found:
         
        midpoint = (first + last)//2
        if item_list[midpoint]== item:
             found = True
        else:
             
             if item < item_list[midpoint]:
                last = midpoint-1
             else:
                first = midpoint+1
        n +=1
         
    return found, n
a =[1,2,3,4,5,6,7,8,9,10,25,26,27,28,29,39,40]
print(binary_search(a, 7))            