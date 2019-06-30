#!/usr/bin/env python
# coding: utf-8

# In[16]:


class List_Queue:
    def __init__(self):
        # Create an empty list to store the values
        self.queue = []
        # Counter variable to keep track of the number of elements in the queue
        self.size = 0
        
    # Function to add data to the queue
    def enqueue(self, data):
        # Make use of the insert method of the list class to add data at the 0th index every time
        self.queue.insert(0, data)
        # Increment the counter upon addition of new data
        self.size += 1
    
    # Function to remove the data from the queue
    def dequeue(self):
        # If the queue contains atleast one value
        if self.size >= 1:
            # Use the pop method of list class to remove the rightmost value from the queue
            data = self.queue.pop()
            # Decrement the counter upon the removal
            self.size -= 1
            return data

