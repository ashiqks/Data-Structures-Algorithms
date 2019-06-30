#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create a node class with next and prev attributes for the queue data structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
        
class Node_Queue():
    def __init__(self):
        # Make the head and tail ends none
        self.head = None
        self.tail = None
        # Counter variable to keep track of the number of elements in the queue
        self.count = 0
        
    # Function to create add the data to the queue
    def enqueue(self, data):
        # Instantiate a node class of the data
        node = Node(data)
        # If the queue is empty
        if not self.head:
            # Make the node as the head and tail
            self.head = node
            self.tail = node
        # If the queue is not empty
        else:
            # Make the to be added node's prev attribute point to the tail node
            node.prev = self.tail
            # Make the next attribute of the tail node point to the to be added node
            self.tail.next = node
            # Make the to be added node as the tail node
            self.tail = node
            
        self.count += 1
        
    # Function to remove a data 
    def dequeue(self):
        data = self.head.data
        # If the queue contains only one element
        if self.count == 1:
            # Make the head and tail point to none
            self.head = None
            self.tail = None
            self.count -= 1
        # If the queue contains more than one element
        elif self.count > 1:
            # Make the current head's next node the head node
            self.head = self.head.next
            # Make the new head's prev attribute to be none
            self.head.prev = None
            
        self.count -= 1
        return data

