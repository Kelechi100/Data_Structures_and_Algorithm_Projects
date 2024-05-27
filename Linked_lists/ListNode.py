"""Creating a  SinglyList NodeClass"""

class ListNode:
    """Represents a singly linked node."""
    def __init__(self, data, next=None):
        """Instantiates a Node with a default next of None."""
        self.data = data
        #Store refrence (next item)
        self.next = None
    """Creating a  Single Linked List Class """
class SinglyLinkedList:
    """Represents a singly linked node."""
    def __init__(self): # This defines two internal class variables named head and tail
        """Creating constructors to initiate this object"""
        self.head = None
        self.tail = None
        """Adding Nodes to a Single_linkedList"""
    def insert_at_end(self, item):
        #Add an item at the end of the list
        if not isinstance(item, ListNode):
            item = ListNode(item)
        if self.head is None:
            self.head = item
            self.tail =  item
        else:
            self.tail.next = item
            self.tail = item
    def output_list(self): # printing the list
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=',' if current_node.next else " " )
            # jump to the linked node
            current_node = current_node.next
    def length_of_list(self):
        #Returns the  number of list items.
        count = 0
        current_node = self.head
        #Trasversing throught the list
        while current_node is not None:
            #incxrease counter by one
            count = count +1
            #jump to the linked node
            current_node = current_node.next
        return count  
    def  unordered_search(self, value, start=0):
        """Seraching the linked list for te node that this value.""" 
        #define current_node
        current_node = self.head
        #define the starting posisiton
        node_id = start
        #defines list of results
        results = []  
        while current_node is not None:
            #if current_node.has_value(value):
            if current_node.data == value:
                results.append(node_id)
            # jump to the linked node
            current_node = current_node.next
            node_id +=1
        return results
    """Removing an Item from the Linked List"""
    def remove_list_item_by_id(self, item_id):
        # Removes the list item with item id
        current_id = 0
        current_node = self.head
        previous_node = None

        while current_node is not None:
            if current_id == item_id:
                #if this is the first node(head)
                if previous_node is  not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next
                    # we don't have to llok any further
                    return
            # needed for the next iteration
            previous_node = current_node
            current_node = current_node.next
            current_id += 1
    """Inserting Items at the beginning"""
    def insert_at_start(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node
    """ Inserting an item After another item"""
    def insert_after_item(self, x, data):
        #Adding an item aftre another item
        current_node = self.head
        while current_node is not None:
            if current_node.data == x:
                break
            current_node = current_node.next
        if current_node is not None:
            new_node = ListNode(data)
            new_node.next = current_node.next
            current_node.next= new_node
            if new_node.next is None:
                self.tail = new_node
    """ Inserting an item before another item"""
    def insert_before_item(self, x, data):
        # Add an item before another item
        if x == self.head.data and self.head:
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == x:
                break
            current_node = current_node.next
        if current_node.next is not None:
            new_node = ListNode(data)
            new_node.next = current_node.next
            current_node.next = new_node
    """ Inserting an item at Specific Index"""
    def insert_at_index(self, index, data):
        # Add an item at the specific index.
        if index == 0:
            new_node = ListNode(data)
            new_node.next = self.head
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return
        i = 0
        Current_node = self.head
        while i < index -1 and Current_node is not None:
            Current_node = Current_node.next
            i = i +1
        if Current_node is not None:
            new_node = ListNode(data)
            new_node.next = Current_node.next
            Current_node.next = new_node
            if new_node.next is None:
                self.tails = new_node
    """ Deleting from the Start"""
    def remove_at_start(self):
        # Removin rhe list item from the start
        if  self.head is None:
            if self.head.next is None:
                self.head = None
                self.tail = None
                
            else:
                self.head  = self.head.next
        else:
             
            #only for testing
            print("The list has no element to delete")


    """ Deleting at the end"""
    def remove_at_end(self):
        """Removes the last item in the list."""
        if self.head is not None:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                while current_node.next.next is not None:
                    current_node = current_node.next
                current_node.next = None
                self.tail = current_node
    """Deleting an item by Value"""
    def delete_by_value(self, x):
        """Removes the item by value."""
        if self.head is not None:
            if self.head.data == x:
                self.head = self.head.next
                if self.head is None:
                    self.tail = None
                return
            current_node = self.head
            while current_node.next is not None:
                if current_node.next.data == x:
                    break
                current_node = current_node.next
            if current_node.next is not None:
                current_node.next = current_node.next.next
                if current_node.next is None:
                    self.tail = current_node

    """Sorting the elements"""
    def sortlist(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        elements.sort(key=lambda x: str(x))
        self.head = None
        self.tail = None
        for data in elements:
            self.insert_at_end(data)
        
    """Merging Sorted List"""
    def merge_sorted(self, other_list):
        current_self = self.head
        current_other = other_list.head
        merged = SinglyLinkedList()

        while current_self is not None and current_other is not None:
            if current_self.data < current_other.data:
                merged.insert_at_end(current_self.data)
                current_self = current_self.next
            else:
                merged.insert_at_end(current_other.data)
                current_other = current_other.next

        while current_self is not None:
            merged.insert_at_end(current_self.data)
            current_self = current_self.next

        while current_other is not None:
            merged.insert_at_end(current_other.data)
            current_other = current_other.next

        return merged

    """Extending the List"""
    def  extend(self, other_list):
        current = other_list.head
        while current:
            self.insert_at_end(current.data)
            current = current.next


    