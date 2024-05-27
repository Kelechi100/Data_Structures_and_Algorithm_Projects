# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:07:15 2024

@author: s22ilogkele
"""

class Item:
    
    """Class for the elements in the priority queue"""
    
    def __init__(self, data, key):
         
         self.data = data
         self.key = key
         
         
    def __str__(self):
        return f'{self.data}, {self.key}'
    
"""Implementation with an Unsorted List"""
    
class UnsortedPriorityQueue:
    def __init__(self):
        self.queue = list()
        
    def enqueue(self, value, key):
        #adds an item to the queue
        self.queue.append(Item(value, key))
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

    def show(self):
        if self.is_empty():
            print("Queue is empty")
            return
        for item in self.queue:
            print(f'({item})', end=" ")
        print()
        
    """function that removes and returns the item with the highest pri
    priority, Here the item with the lowest value is considered 
    to have the highest priority"""
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            highest_priority_index = 0
            #finding the index of thye item with the highest priority
            for i in range (1, len(self.queue)):
                if(self.queue[i].key < 
                       self.queue[highest_priority_index].key):
                    highest_priority_index = i
            # remove and return the item with the hihgest priority
        return self.queue.pop(highest_priority_index)
        
        
    """Peeking at the higghest priority item without removing it"""
    def peek(self):
        if  self.is_empty():
            return None
        else:
            highest_priority_index = 0
            #Finding the index of the item with the highest priority
            for i in range (1, len(self.queue)):
                if(self.queue[i].key < 
                       self.queue[highest_priority_index].key):
                    highest_priority_index = i
            # retruning the item with the highest priority
        return self.queue[highest_priority_index]
                