#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Create the hash class with key and value as attributes
class Hash_Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        
# Class for chaining hash table
class Chaining_Hash_Table:
    def __init__(self, size):
        self.size = size 
        # Initialize list of empty lists to store the items 
        self.slot = [[] for i in range(self.size)]
        self.count = 0
        
    # Function to create hash value of the key
    def _hash(self, key):
        mult = 1
        hash_value = 0
        for c in key:
            hash_value += (mult * ord(c))
            mult += 1
        return hash_value % self.size
    
    # Function to insert the items 
    def put(self, key, value):
        # Generate the hash value using the key
        h = self._hash(key)
        # If key is already used
        if self.get(key):
            # Iterate over the lists
            for i in self.slot[h]:
                # Find the item and update the value
                if i.key == key:
                    i.value = value
                    return
        # If the key is new create new hash item and insert it at the appropriate slot
        item = Hash_Item(key, value)
        self.slot[h].append(item)
        self.count += 1
        
    # Function to get the value using the key
    def get(self, key):
        # Get the hash value of the key
        h = self._hash(key)
        # Iterate over the slots
        for item in self.slot[h]:
            # If key found return the value
            if item.key == key:
                return item.value
        return None
    
    # Function to delete the item
    def delete(self, key):
        # If key is not already present raise an error
        if not self.get(key):
            raise Exception('Key not found')
        # Get the hash of the key
        h = self._hash(key)
        for item in self.slot[h]:
            # If the item is found delete it
            if item.key == key:
                self.slot[h].remove(item)
                self.count -= 1
    
    # Magic function to set the value
    def __setitem__(self, key, value):
        self.put(key, value)
        
    # Magic function to get the value
    def __getitem__(self, key):
        return self.get(key)

