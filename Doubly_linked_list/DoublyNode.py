# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:54:43 2024
creating a doubly linked list 

@author: s22ilogkele
"""
class DoublyNode:
    """Reprsents a doubly linked node."""
    def __init__(self, data):
        """Instantiates a doublylinkedList object"""
        self.data = data
        self.next = None
        self.previous = None
class DoublyLinkedList:
    """Represntd a doubly linked list."""
    def __init__(self):
        """Instantiates a DOublyLinkedList Object"""
        self.head = None
        
        """Traversing a Doubly Linked List"""
    def print_list(self):
        """Prints the elements of the doubly linked list"""
        if self.head is not None:
            current = self.head
            while current is not None:
                #while current
                print(current.data, end=" ")
                current = current.next
            print()
        else:
            #only for testing
            print('List has no element')         
    """Inserting Items at the beginning."""
    def insert_at_start(self, data):
        """Insert a node at the front of the doubly list"""
        #Allocating memory for new node
        new_node = DoublyNode(data)
        
        if self.head is None:
            #If the list is empty
            self.head = new_node
        else:
            #If the list is not empty
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
    """Iserting Items at the end """
    def insert_at_end(self, data):
        """Insert a new node at the end of the list"""
        new_node = DoublyNode(data)
        if self.head is None:
            #if the linked list is empty
            self.head = new_node
        else:
            #if the linked list is not empty
            current = self.head
            while current.next is not None:
                #traverse to the end of the linked list
                current = current.next
            # Now, the last node of the list is current
            current.next = new_node
            
            #Assinging previous of new_node to current
            new_node. previous  =  current


    """Inserting Item after Another Item"""
    def insert_after_item(self, item, data):
        """Inserting a new node after another item"""
        if self.head is not None:
          
          #if the linked list is not empty
          current = self.head

          while current is not None:
              
            #Iterate through the nodes in the list
            if current.data != item:
                  
                current = current.next
            else:
                #The node is found
                  
                new_node = DoublyNode(data)
                new_node.previous = current
                new_node.next = current.next
                if current.next is not None:
                  current.next.previous = new_node
                current.next = new_node   
                break
            if current is None:
                    print("Item not found")
                    #the nod eis not found
                    # Omly for testing
                    print("Item is not in the list")
        else:
            #Only for testing   
            print("List is empty")
    """ Inserting Item Before Another Item"""
    def insert_before_item(self, target_data,new_data):
        """Inserting a new node before another item"""
        if self.head is not None:
            #if the linked list is not empty
            new_node = DoublyNode(new_data)
            if self.head.data == target_data:
                #If the head contains the target data then
                #set the next of new Node to head
                new_node.next = self.head
                self.head.previous = new_node
                self.head = new_node
                return
            current = self.head
            while current:
                if current.data == target_data:
                    new_node.previous = current.previous
                    new_node.next = current
                    current.previous.next = new_node
                    current.previous = new_node
                    return
                current = current.next
    
    """Deleting Elements From the Start"""
    def delete_at_start(self):
        """Deleting the first node from the doubly linked list"""
        if self.head is not None:
            #if the list is not empty
            if self.head.next is None:
                self.head = None
                return
            # The list contain more than one elemnts
            self.head  = self.head.next
            self.head.previous = None
        else:
            #only for testing
            print("The list has no element o delete")
    """Deleting Elements From the End"""
    def delete_at_end(self):
        if self.head is not None:
            #if  the list is not empty
            if not self.head.next:
                #If the list contain only one element
                self.head = None
                return
            #The list contain more than one element
            previous = None
            current = self.head
            while current.next:
                prev = current
                current = current.next
            prev.next = None
        else:
            #only for testing
            print("The list has  no elements to delete")

            


                      
                
                
                      
              
              
                
                
        
        
            