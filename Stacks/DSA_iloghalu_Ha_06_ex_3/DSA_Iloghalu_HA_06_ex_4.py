# A program that removes all adjacent duplicates in string of lowercase letters.

from collections import deque

def remove_adjacent_duplicates(s):
    stack = deque()

    for char in s:
        if not stack or char != stack[-1]:
            stack.append(char)
        else: 
            stack.pop()
    return ''.join(stack)


# Test Cases
letters = deque()
letters =  input("Enter as many duplicate letters as you wish: ")#"abbaca"
#s2 = "oazxxzay"
print(f"Duplicate letters removed: {remove_adjacent_duplicates(letters)}")  # Output: "ca"
#print(remove_adjacent_duplicates(s2))  # Output: "oy"

