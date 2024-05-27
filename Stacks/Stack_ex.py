class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

def check_balanced_brackets(expression):
    stack = Stack()
    brackets_map = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in brackets_map.values():
            stack.push(char)
        elif char in brackets_map.keys():
            if stack.is_empty() or brackets_map[char] != stack.pop():
                return "Not Balanced"
    
    if stack.is_empty():
        return "Balanced"
    else:
        return "Not Balanced"
    

   