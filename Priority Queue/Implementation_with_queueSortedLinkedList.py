# -*- coding: utf-8 -*-
"""
Created on Thu May  2 13:12:49 2024

@author: s22ilogkele
"""

class PriorityQueueNode:
    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.next = None
    def __str__(self):
        return f'{self.data}, {self.key}'
    
class sortedPriorityQueue:
    def __init__(self):
        self.front = None
        self.number_of_items = 0
        
    def enqueue(self, value, key):
        #adds an item to the queue
        new_node = PriorityQueueNode(value, key)
        if self.is_empty():
            self.front = new_node
        else:
            if self.front.key > key:
                new_node.next = self.front
                self.front = new_node
            else:
                current = self.front
                while current.next:
                    if key < current.next.key:
                        break
                    current = current.next
                    
                new_node.next = current.next
                current.next = new_node
        self.number_of_items += 1
        
        
    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self.number_of_items

    def show(self):
        if self.is_empty():
            print("Queue is empty")
            
        else:
           current = self.front
           while current:
               print(f'({current}) ' , end =" ")
               current = current.next
           print()
        
    """function that removes and returns the item with the highest pri
    priority, Here the item with the lowest value is considered 
    to have the highest priority"""
    
    def dequeue(self):
       if self.is_empty():
           return None
       else:
          first = self.front
          self.front = self.front.next
          self.number_of_items -= 1
          return first
    """Peeking at the higghest priority item without removing it"""
    def peek(self):
        if  self.is_empty():
            return None
        else:
            return self.front
   