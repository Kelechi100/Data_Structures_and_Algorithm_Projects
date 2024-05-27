# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:01:45 2024

@author: s22ilogkele
"""

# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:07:15 2024

@author: s22ilogkele
"""

class Item:
    
    """Class for the elements in the priority queue
    Ascending Order of Priority queue -> The item with the lowest key(priority )
    value is considered to have the higest priority
    """
    
    def __init__(self, data, key):
         
         self.data = data
         self.key = key
         
         
    def __str__(self):
        return f'{self.data}, {self.key}'
    
"""Implementation with an sorted List in ascending order"""
    
class sortedPriorityQueue:
    def __init__(self):
        self.queue = list()
        
    def enqueue(self, value, key):
        #adds an item to the queue
        new_item = Item(value, key)
        index = 0
        while index < len(self.queue) and self.queue[index].key <= key:
            index +=1
        self.queue.insert(index, new_item)
        
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
           return self.queue.pop(0)
    """Peeking at the higghest priority item without removing it"""
    def peek(self):
        if  self.is_empty():
            return None
        else:
            return self.queue[0]