#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Create the hash class with key and value as attributes
class Hash_Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# In[54]:


# Create the hash table class
class Hash_Table:
    def __init__(self, size):
        self.size = size 
        # Initialize an list with None values equal to number of the input size 
        self.slot = [None for i in range(self.size)]
        self.count = 0
    
    # Function to create hash of the key
    def _hash(self, key):
        mult = 1
        hash_value = 0
        for c in key:
            hash_value += (mult * ord(c))
            mult += 1
        return hash_value % self.size
    
    # Function to create put the key and value into the hash table
    def put(self, key, value):
        # Create the hash of the key using the _hash functin
        h = self._hash(key)
        # Create a hash item
        item = Hash_Item(key, value)
        # Iterate over the hash list
        while self.slot[h]:
            # If the key is already present, break
            if self.slot[h].key == key:
                break
            # hop to next available slot by increasing the hashed index
            h = (h + 1) % self.size
        # If empty slot found insert the item
        if not self.slot[h]:
            self.count += 1
        self.slot[h] = item
    
    # Function to get an item using the key
    def get(self, key):
        # Produce the hash of the key
        h = self._hash(key)
        # Iterate over the slots
        while self.slot[h]:
            # If key is found return the value
            if self.slot[h].key == key:
                return self.slot[h].value
            # If the value is not found at the slot increment the hash value by one to iterate over
            h = (h + 1) % self.size
        return None
    
    # Function to delete an item
    def delete(self, key):
        # Get the hash value
        h = self._hash(key)
        # Iterate over the slots
        while self.slot[h]:
            # If key is found delete the item
            if self.slot[h].key == key:
                del self.slot[h]
                self.count -= 1
                return
            h = (h + 1) % self.size
        raise Exception('Key not found')
    
    # Magic function to set the value using the key
    def __setitem__(self, key, value):
        self.put(key, value)
    
    # Magic function to get the value using the key
    def __getitem__(self, key):
        return self.get(key)
    

