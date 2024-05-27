# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 10:06:58 2024

@author: s22ilogkele
"""

from stack import Stack
my_stack = Stack(3)
my_stack.push(38)
my_stack.push(27)
my_stack.push(25)
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