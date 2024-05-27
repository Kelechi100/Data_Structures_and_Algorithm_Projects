# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:10:20 2024

@author: s22ilogkele
"""
from Linked_satck import Stack
my_stack = Stack(3)
my_stack.push(8)
my_stack.push(7)
my_stack.push(2)
#my_stack.push(40)

print(f"My stack {my_stack}")
print(f"My stack is empty:{my_stack.is_empty()}")
print(f"My stack is full: {my_stack.is_full()}")
print(f"current size of my stack : {my_stack.current_size()}")
# poping a  stack
print("---------------------------\n")
print("STACK ELEMENTS AFTER BEEN POPPED\n")
last_item = my_stack.pop()
print(f"Pop item (last): {last_item}")
print(f"My stack {my_stack}")
my_stack.current_size()
print(f"current size of my stack : {my_stack.current_size()}")
print(f"My stack is empty:{my_stack.is_empty()}")
print(f"My stack is full: {my_stack.is_full()}")