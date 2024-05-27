# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 09:46:50 2024

@author: s22ilogkele
"""

from collections import deque
numbers  = deque(maxlen =5)
 # stack
 
numbers.append(99)
numbers.append(18)
numbers.append(29)
numbers.append(27)
numbers.append(93)
numbers.append(80)
numbers.append(23)
numbers.append(55)
print(f'numbers:{numbers}')

numbers.append(18)
print(f'numbers:{numbers}')
last_item = numbers.pop()
print(f'Pop items (last): {last_item}')
print(f"Numbers after popping: {numbers}")

#You can dequeue like a dueue
first_item = numbers.popleft()
print(f'Pop items (first): {first_item}')
print(f"Numbers after dequeueing:{numbers}")