# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:38:22 2024

@author: s22ilogkele
"""

from implemetation_item import UnsortedPriorityQueue

# Testing  unsorted Ascending Order priority Queue
my_priority_queue = UnsortedPriorityQueue()
my_priority_queue.enqueue(4, 2)
my_priority_queue.enqueue(5, 3)
my_priority_queue.enqueue(6, 4)
my_priority_queue.enqueue(7, 1)
my_priority_queue.show()

print("the unsorted priority queue: ")
my_priority_queue.show() 

# checking the top elements using the peek method
print(f"the top element is:({my_priority_queue.peek()})")
print(f"The size of queue is :{my_priority_queue.size()} ")
print("")
my_priority_queue.dequeue()
my_priority_queue.show()
