# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:59:04 2024

@author: s22ilogkele
"""
import random
from MinHeap import MinHeap
# exmaple usage
my_heap = MinHeap()

#printing(my_heap)
my_heap.show()

print("Inserting")


for i in range(0,8):
   randum_num = random.randint( 1, 10)
   
   #adding the random numbers to the heap
   my_heap.insert(randum_num)
   print(f" added  {randum_num}, heap after iteration:",  my_heap)
  
print("Heap Iterating through the elements")
# removing smallest node from the element
my_heap.show()
#Printing each  heap item its degree, left child, right child, and min child
for i in range(0,8):
   print(f" Heap node {i} degree: {my_heap.degree(i)}, left child: {my_heap.left_child(i)}, right child:
         
         {my_heap.right_child(i)}, min child: {my_heap.min_child(i)} ")
my_heap.show()


