#Hot potatoe games

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.tail = None
        self.size =  0

    def enqueue(self, data):
        new_node  = Node(data)
        if self.tail is None:
            self.tail = new_node 
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node 
        self.size += 1

    def dequeue(self):
        if self.size is None:
            return None
        head = self.tail.next
        if self.tail == head:
            self.tail = None
        else:
            self.tail.next = head.next
        self.size -= 1
        return head.data
    
    def rotate(self, k):
        if self.tail is None or k <=0:
            return
        for _ in range(k):
            self.tail = self.tail.next

    def get_size(self):
        return self.size
    
    def print_queue(self):
        if self.tail is None:
            print("Queue is empty")
            return
        current = self.tail.next
        data = []
        while True:
            data.append(str(current.data))
            current = current.next
            if current == self.tail.next:
                break
            print(" ".join(data))
            
