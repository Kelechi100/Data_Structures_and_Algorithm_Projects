#implementing stack method using arrays
class Stack:
    def __init__(self, size): 
        self.size = size
        self.stack = [None]  * size
        self.top = -1

    #function to add an item to the top
    def push(self, item):
        if self.stack == self.size -1:
            raise Exception('stack overflow')
        else:
            self.top += 1
            self.stack[self.top] = item
    # to delete an item from the top
    def pop(self):
      if self.top == -1:
        raise Exception('stack underflow')
        item = self.stack[self.top]
        self.top -= 1
        return item
      
    # method to check the hihest value
    def peek(self):
       if self.top == -1:
          raise Exception('stack underflow')
          return self.stack[self.top]
       
    #methods to check and return the current size of items in the stack
    def size(self):
       return self.top + 1
    
    # output the stack content
    def print_stack(self):
       return self.stack
    
    def __str__(self):
       return self.stack
    

    def main():
       stack = Stack(5)
       stack.push(1)
       stack.push(2)
       stack.push(3)
       stack.push(4)
       stack.print_stack()
       
    
    
        



