class Node:
    
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
    
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
                    
    def __iter__(self):
        self._iter_node = self.head
        return self

    def __next__(self):
        if self.iter_node == None:
            raise StopIteration
        ret = self.iter_node.data
        self.iter_node = self.iter_node.next
        return ret
        
    def prepend(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    def length(self):
        return self.length
    
    def __str__(self):
        return str([value for value in self])