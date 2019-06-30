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


# Class for doubly-linked list
class Doubly_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    # Fucntion to append a data to the list
    def append(self, data):
        node = Node(data)
        # Checking  and adding the data if the list is empty
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            # If the list is not empty then add the data nodes at the end of the list
            node.prev = self.tail
            self.tail.next = node 
            self.tail = node
        self.count += 1
            
    # Function to iterate over the nodes in the list to print the values
    def iteration(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
            
    # To check if a particular data is found in the list with the help of iteration function
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
    
    # Function to set the value of a particular node using the index
    def __setitem__(self, index, data):
        if index > (self.count-1):
            raise Exception('Index out of range')
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data
        
    
    # Funciton to delete a node in the list using the index
    def delete_by_data(self, data):
        current = self.head 
        node_deleted = False 
        # If the item is not in the list
        if current is None:       
            node_deleted = False 
        
        # If the node to be deleted is at the beginning of the list
        elif current.data == data:   
            self.head = current.next  
            self.head.prev = None 
            node_deleted = True 
        
        # If the node to be deleted is at the end of the list 
        elif self.tail.data == data:   
            self.tail = self.tail.prev  
            self.tail.next = None 
            node_deleted = True 
        # Search item to be deleted, and delete that node 
        else: 
            while current:          
                if current.data == data: 
                    # Make the next attribute of the current's previous node point to next attribute of the current node
                    current.prev.next = current.next  
                    # Make the previous attribute of the current's previous node point to the previous attribute of the current node
                    current.next.prev = current.prev 
                    node_deleted = True 
                current = current.next 

        if node_deleted: 
            self.count -= 1
    
    # Function to delete a node using the index
    def delete_by_index(self, index):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        # If the node is at the beginning of the list
        elif index == 0:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        # If the node is at the end of the list
        elif index == (self.count-1):
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            for i in range(self.count-1):
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

