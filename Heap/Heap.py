#!/usr/bin/env python
# coding: utf-8

# In[7]:


"""
Example to make a minimum heap data structure using Python.
Implemented insert and pop functions along with helper functions.

"""

# Class to implement min heap data structure
class Heap:
    def __init__(self):
        # List to hold the values in the heap, initialized with zero to represent the dummy first element
        self.heap = [0]
        # Variable to keep track of the size of the heap
        self.size = 0
    
    # Function to reorder the heap after inserting new element, the parameter is the size of the heap, that is the index of the inserted element
    def balance(self, k):
        # Checking if the index is root index, if not loop over until then
        while k // 2 > 0:
            # Checking if the inserted element is smaller than its parent
            if self.heap[k] < self.heap[k//2]:
                # If the inserted element is smaller than its parent, rearrange the values
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            # Update the index
            k //= 2
    
    # Function to insert an element
    def insert(self, item):
        # Append the element to the heap
        self.heap.append(item)
        # Increase the size variable of the heap by one
        self.size += 1
        # Balance the heap after inserting new element
        self.balance(self.size)
    
    # Helper function to reorder the heap after deleting an element, param is the root element index 
    def sink(self, k):
        # Loop over until the changing index value is less than the size of the heap
        while k * 2 <= self.size:
            # If the right child index is out of index, get the index of the left child
            if (k * 2 + 1)> self.size:
                m = k * 2
            # if the left child is lesser is than right child, get the index of left child or vice-versa
            elif self.heap[k*2] < self.heap[k*2+1]:
                m = k * 2 
            else:
                m = k * 2 + 1
            # Check if the parent is greater than child, if yes, change thea values
            if self.heap[k] > self.heap[m]:
                self.heap[k], self.heap[m] = self.heap[m], self.heap[k]
            # Make the new value of the parent to be the index of its child
            k = m
    
    # Function to delete and pop off the values in the min heap
    def pop(self):
        # Get the min value of the heap
        item = self.heap[1]
        # Make the last value of the heap as the root
        self.heap[1] = self.heap[self.size]
        # Reduce the size variable of the heap by one
        self.size -= 1
        # Pop the last child value off the heap which was made the root
        self.heap.pop()
        # Rearrange the heap
        self.sink(1)
        return item
                
h = Heap()
for i in (4, 8, 7, 2, 9, 10, 5, 1, 3, 6):
    h.insert(i)

print(h.heap)

for i in range(10):
    n = h.pop()
    print(n)
    print(h.heap)

