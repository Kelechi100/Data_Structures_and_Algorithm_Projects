# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:48:47 2024

@author: s22ilogkele
Implementing a Stack class Using an Array
"""

class Stack:
    
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
         
        """ Using the push method"""
    def push(self, item):
        if self.top == self.size - 1:
                
            raise Exception("stack Overflow")
                
        self.top += 1
        self.stack[self.top] = item
            
    def pop(self):
        if self.top == -1:
            raise Exception("stack Overflow")
        item = self.stack[self.top]
        self.top -= 1
        return item
    
    def peek(self):
        if self.top == -1:
            raise Exception("stack is empty")
            return self.stack[self.top]
        
    def current_size(self):
        return self.top + 1
    
    def __str__(self):
        return str(self.stack[: self.top +1 ])
    
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return  self.top == self.size -1 
    
        
        