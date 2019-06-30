#!/usr/bin/env python
# coding: utf-8

# In[235]:


# Class to create a node for singly-linked list
class Node:
    def __init__(self, data):
        # Variable to hold the data point
        self.data = data                 
        # Reference for the next node
        self.next = None


# In[252]:


class SinglyLinkedList:
    # singly-linked list 
    def __init__(self):
        # Create an empty list with the tail and head nodes as None
        self.tail = None
        self.head = None
        # Counter to keep the number of values in the list
        self.count = 0
    
    # Function to add a data point to the list
    def append(self, data):
        # create an object of the node
        node = Node(data)
        # If linked list already contains values then make the head pointing to the currently being added node  
        if self.head:
            self.head.next = node
            self.head = node
        # If the list is empyt initially then make it point to the tail point 
        else:
            self.tail = node
            self.head = node
        self.count += 1
        
    # Function to delete a value from list
    def delete_by_data(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                # Checking if the value to be deleted is the first node
                if current == self.tail:
                    self.tail = current.next
                # Checking if the value to be deleted is the last node
                elif current == self.head:
                    self.head = prev
                    prev.next = None
                # Values to deleted between the first and last nodes
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next
    
    # Function to delete a data point using the index of it
    def delete_by_index(self, index):
        if index > (self.count-1):
            raise Exception('Index out of range')
        current = self.tail
        prev = self.tail
        for i in range(self.count):
            if i == index:
                # If the node is at the 0th index
                if i == 0:
                    self.tail = current.next
                # If the node is at the last index
                elif i == (self.count-1):
                    self.head = prev
                    prev.next = None
                else:
                    prev.next = current.next
                self.count -= 1
                return
            prev = current
            current = current.next
    
    # Function to iterate over the nodes in the list 
    def iteration(self):
        # Make the current variable equal the first node
        current = self.tail
        # Iterate using the while loop till next attribute of the current node is none
        while current:
            val = current.data
            current = current.next
            yield val
    
    # Function to search if a particular data is in the list or not
    def search(self, data):
        # Making use of the iteration function to chech if the data point is included
        for d in self.iteration():
            if d == data:
                return True
        return False
    
    # Using the __getitem__ magic function to return a data node using the index
    def __getitem__(self, index):
        if index > (self.count-1):
            raise Exception("Index out of range")
        current = self.tail
        for i in range(index):
            current = current.next
        return current.data
    
    # Using the __setitem__ magic function to set a data at a particular index
    def __setitem__(self, index, data):
        if index > (self.count-1):
            raise Exception('Index out of range')
        current = self.tail
        for i in range(index):
            current = current.next
        current.data = data
        
    # Function to reverse the values in the list
    def reverse(self):
        current = self.tail
        # Initialise a stack to hold the data points inorder to hold the values 
        stack = Stack()
        # Push the values from the beginning to end of the list to stack
        for i in range(self.count):
            stack.push(current.data)
            current = current.next
        current = self.tail
        # Pop the values in the stack onto the list from the beginning to the end so as to reverse the list
        for i in range(self.count):
            current.data = stack.pop()
            current = current.next
            


# In[254]:


# Class for stack
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    # Function to store the data in the stack
    def push(self, data):
        node = Node(data)
        # Checking if the stack is empty or not
        if self.top:
            # If not empty make the current top node pointing to the newly added node
            node.next = self.top
            # Make the newly added node as top
            self.top = node
        else:
            # If stack is already empty make the node top
            self.top = node
        self.size += 1    
    
    # Function to remove data from the stack
    def pop(self):
        # Checking if there is any node present in the stack 
        if self.top:
            data = self.top.data
            self.size -= 1
            # If the current top node contains the next attribute then make the next node as top
            if self.top.next:
                self.top = self.top.next
            # If not then top is none
            else:
                self.top = None
            return data
        else:
            return None
    
    # Function to see the value without removing the data
    def peek(self):
        if self.top:
            return self.top.data


# In[11]:


# Node class for doubly-linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


# In[225]:


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


# In[229]:


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

