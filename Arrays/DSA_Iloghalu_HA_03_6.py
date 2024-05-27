#Excerise 6: Creating a dynamic arrays
class MydynamicArray:
    # initializing empty list to store elemnts
    def __init__(self):
        self.size = 0
        self.capacity = 1
        self.array = [None] * self.capacity
    def __str__(self):
        return str(self.array[:self.size])
    #implementing append method
    def append(self, item):
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.size] = item
        self.size += 1
    #implemting the insert method
    def insert(self, index, item):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")
        if self.size == self.capacity:
            self.resize(2 * self.capacity)
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = item
        self.size += 1
    #implementing the pop method
    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        popped_element = self.array[self.size - 1]
        self.size -= 1
        if self.size <= self.capacity // 4:
            self.resize(self.capacity // 2)
        return popped_element
    #implementing the remove method
    def remove_item(self, item):
        index = None
        for i in range(self.size):
            if self.array[i] == item:
                index = i
                break
        if index is not None:
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            if self.size <= self.capacity // 4:
                self.resize(self.capacity // 2)
        else:
            raise ValueError("Element not found in array")

    #implemting the index method to search for arrays
    def index(self, item):
        self.data.index()        
    #implementing the resize  method to resize the array when its full or 
        #or when it is reduced.
    def resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    #implementing print for output
    def display(self):
        print(self.data)
