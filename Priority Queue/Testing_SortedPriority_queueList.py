# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:02:18 2024

@author: s22ilogkele
"""

from implement_sortedList import sortedPriorityQueue

# Testing  unsorted Ascending Order priority Queue
my_priority_queue = sortedPriorityQueue()
my_priority_queue.enqueue(4, 2)
my_priority_queue.enqueue(5, 3)
my_priority_queue.enqueue(6, 4)
my_priority_queue.enqueue(7, 1)
my_priority_queue.enqueue(8, 5)
my_priority_queue.enqueue(9, 10)
my_priority_queue.enqueue(10, 9)

print("List of the the sorted priority queue in ascending order : ")
my_priority_queue.show() 

# checking the top elements using the peek method
print(f"the top element  in the priority queue is:({my_priority_queue.peek()})")
print(f"The size of queue is :{my_priority_queue.size()} ")

print(f"Is my Queue Empty: {my_priority_queue.is_empty()} ")
print("-----------------------------------------------------")
print("Sorting in ascending order to remove the highest element in the priority queue")
my_priority_queue.dequeue()
my_priority_queue.show()
print(f"The size of queue is :{my_priority_queue.size()} ")



