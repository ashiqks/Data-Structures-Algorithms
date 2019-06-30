#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Node class for stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# In[11]:


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

