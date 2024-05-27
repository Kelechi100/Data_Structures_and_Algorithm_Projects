# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:21:00 2024

@author: s22ilogkele
"""
class MinHeap(object):
    """Changing the init method"""
    def __init__(self, new_list=None):
        if new_list is None:
            #creates an empty heap
            self.heap = []
        else:
            #builds the heap from the list in place
            self.build_heap(new_list)
        self.current = 0
        
    # definingif the size is empty
    def __len__(self):
        # Retruns the number of items in the heap
        return len(self.heap)
    
    def size(self):
        #returns number of items in the heap
        return len(self.heap)
    
    def is_empty(self):
        #returns True if the heap is empty
        return len(self.heap) == 0
    
    
    
    """Defininf the helper methods"""
    
    def has_parent(self, i):
        # returns True if the node has parent
        return i > 0
    
    def has_left_child(self, i):
        #returns True if the node has left child
        return 2 * i + 1 < self.size()
    
    def has_right_child(self, i):
        #returns True if the node has a right child
        return 2 * i + 2 < self.size()
    
    """Methods that return the index of the parent or child node"""
    def parent_index(self, i):
        #returns the index of the node's parent
        if self.has_parent(i):
            return(i-1) // 2
        return None
    
    def left_child_index(self, i):
        #returns the index of the node's left child
        if self.has_left_child(i):
            return 2 * i + 1
        else:
            return None
        
    def right_child_index(self, i):
        #returns the index of the node's right child
        if self.has_right_child(i):
            return 2 * i + 2
        else:
            return None
        
    """Methods that returns the value(key) of a parent or child node"""
    def parent(self, i):
        #retruns the node's parent
        if self.has_parent(i):
            return self.heap[self.parent_index(i)]
        return None
    
    def left_child(self, i):
        #reteuns the node's left child
        if self.has_left_child(i):
            return self.heap[self.left_child_index(i)]
        else:
            return None
        
    def right_child(self, i):
        #returns the node's right child
        if self.has_right_child(i):
            return self.heap[self.right_child_index(i)]
        else:
            return None
        
    """Methods that help determo=ine the smallest of the childern(1) """
    def min_child_index(self, i):
        #Returns the index of the node's smallest child
        #if the current node has no children
        if not self.has_left_child(i):
            return None
        # oif thge current node has only one child,
        #return the index of the unique (left)child
        if self.left_child_index(i) == self.size() -1 :
            return self.left_child_index(i)
        else:
            #the current node has two children
            #Return the index of the min child
            if self.left_child(i) < self.has_right_child(i):
                return self.left_child_index(i)
            else:
                return self.right_child_index(i)
            
    """Methods that help determine the smallest of children(2) """
    def min_child(self, i):
        # REturns the node's sma;llest child

        if self.min_child_index(i) is None:
            return None
        else:
            return self.heap[self.min_child_index(i)]
        
    """Swapping methods"""
    def swap_nodes(self,  n1, n2):
        """Swaps the two given nodes of the heap.
        This method will be needed for heapify and insertion
        to swap nodes that are not in order"""
        
        self.heap[n1], self.heap[n2] = self.heap[n2], self.heap[n1]
        
        
    """Insertion Operation"""
    def insert(self, item):
        #Inserts an item into the heap.
        #Append the item to the heap
        self.heap.append(item)
        #Move the item to its position from bottom to the rop
        self.heapify_up(len(self.heap) - 1 )
        
    def heapify_up(self, i):
        """Moves the item up in the tree to maintain
        the heap property"""
        #while the item is not the root or is less than parant
        stop = False
        while(i != 0) and not stop:
            #if the item is less than its parent swap the nodes
            if self.heap[i] < self.parent(i):
                self.swap_nodes(i, self.parent_index(i))
            else:
                stop = True
            #Moves the index to the parent to keep the properties
            i = (i -1) // 2
    """Deleting from the MinHeap"""
    def delete_min(self):
        """Deletes the highest priority element from the heap"""
        if self.is_empty():
            return None
        
        min_value = self.heap[0]
        #copy the last item to the first position
        self.heap[0] = self.heap[-1]
        #Remove the last item
        self.heap.pop()
        #Move down the first item to its correct positio
        self.heapify_down(0)
        return min_value
    
    def heapify_down(self, i):
        """Moves the item down in the tree to maintain the heap position"""
        #if the current node has at least one child
        while self.min_child_index(i):
            #get the index of the min child of the current node
            mc_index= self.min_child_index(i)
            #swap the nodes, if the current item is greater than its min child
            if self.heap[i] > self.min_child(i):
                self.swap_nodes(i, self.min_child_index(i))
            i = mc_index
            
            
    def show(self):
        #prints all the elemnts of the  minheap
        if self.is_empty():
           print("Heap is empty")
           return
        for item in self.heap:
               print(f'{item}', end=" ")
        print() 
        
    def get_min(self):
        #Returns the smallest item from the heap
        
        if self.size() == 0:
            return None
        return self.heap[0]
    
    """Using the heapify or build the heap"""
    def build_heap(self, new_list):
        #Builds the heap in place
        self.heap = list(new_list)
        #Start out in the middle of the tree
        i = (len (new_list) - 1 ) // 2
        #Continue towards the root
        while i >= 0:
            #Move down the current  node to its coreect position in the heap
            i = i- 1
            
    def __str__(self):
        return str(self.heap)
    
    def __iter__(self):
       return  self
            
    def __next__(self):
        if self.current >=  len(self.heap):
            item= self.heap[self.current]
            self.current += 1
            return item
        else:
            raise StopIteration
            
            
    
            
       
  
                               
    
        
    
        
        