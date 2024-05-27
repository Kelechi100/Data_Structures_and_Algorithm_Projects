# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:08:14 2024
IMPLEMENTING A STACK CLASS USING LINKED LISTS
@author: s22ilogkele
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next =  None
        
class Stack:
    def __init__(self, max_size = None):
        self.top = None
        self.curr_size = 0 # while stack is empty  = 0
        self.max_size = max_size
        
    def push(self, item):
        if self.is_full():
            raise Exception("stack Underflow")
        node = Node(item)
        if self.top:
            node.next =  self.top
        self.top = node
        self.curr_size += 1
        
    def pop( self):
        if not self.top: 
            raise Exception("stack underflow")
            item =  self.top.data
            self.top= self.top.next
            self.curr_size= self.curr_size - 1
            return item
        
        
    def peek(self):
        if  not self.top:
            raise Exception("stack is empty")
        return self.top.data
    
    def current_size(self):
        return self.curr_size
    
    
    def print(self):
        current_node = self.top
        while current_node is not None:
            # jump to the lined node
            print(current_node.data, end= " ")
            current_node = current_node.next
        print()
        
    def is_full(self):
        
        if self.max_size is not None:
            
            return self.curr_size == self.max_size
        return True
    
    def is_empty(self):
        return self.curr_size == 0
    
    def __str__(self):
        stack_str = ""
        current_node =  self.top
        while current_node is not None:
            # jump to the lined node
            #print(current_node.data, end= " ")
            stack_str += f'{current_node.data}' 
            current_node = current_node.next
        return stack_str
    
    