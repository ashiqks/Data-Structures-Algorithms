#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Node class for doubly-linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


# In[ ]:


# Class for the circular doubly-linked list
class Circular_Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    # Function to add a node to the list
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node 
            self.tail = node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.count += 1
            
    # Iterate over the list to return the values one by one
    def iteration(self):
        current = self.head
        for i in range(self.count):
            val = current.data
            current = current.next
            yield val
    
    # Search if a particular value is found at the list 
    def search(self, data):
        for d in self.iteration():
            if d == data:
                return True
        return False
    # Use of the magic functions to get a particular value using the index point
    def __getitem__(self, index):
        if index > (self.count-1):
            raise Exception("Index out of range")
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
    # Using the __setitem__ magic function to set a data at a particular index
    def __setitem__(self, index, data):
        if index > (self.count-1):
            raise Exception('Index out of range')
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data
        
    def delete_by_data(self, data):
        current = self.head 
        node_deleted = False 
        if current is None:       
            node_deleted = False 
        # If the node to be deleted is at the beginning
        elif current.data == data:   
            self.head = current.next  
            self.head.prev = self.tail
            self.tail.next = self.head
            node_deleted = True 
        # If the node to be deleted is at the last 
        elif self.tail.data == data:
            self.tail = self.tail.prev  
            self.tail.next = self.head
            self.head.prev = self.tail
            node_deleted = True 
        else: 
            # If the node to be deleted is in between the first and last nodes of the list
            for i in range(1, self.count-1):          
                if current.data == data: 
                    current.prev.next = current.next  
                    current.next.prev = current.prev 
                    node_deleted = True 
                current = current.next 

        if node_deleted: 
            self.count -= 1
    # Function to delete a data point using the index 
    def delete_by_index(self, index):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        # If the node is at the beginning of the list
        elif index == 0:
            self.head = current.next
            self.head.prev = self.tail
            self.tail.next = self.head
            node_deleted = True
        # If the node is at the end of the list
        elif index == (self.count-1):
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            node_deleted = True
        else:
            for i in range(1, self.count-1):
                if i == index:
                    # Make the next attribute of the current's previous node point to next attribute of the current node
                    current.prev.next = current.next
                    # Make the previous attribute of the current's previous node point to the previous attribute of the current node
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count -=1
    # Function to reverse the list
    def reverse(self):
        current = self.head
        end = self.tail
        # Iterate over till the half index of the list and exchange the data between nodes in the list so as to reverse the list
        for i in range(self.count//2):
            current.data, end.data = end.data, current.data
            current = current.next
            end = end.prev

