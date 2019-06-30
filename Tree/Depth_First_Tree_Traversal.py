#!/usr/bin/env python
# coding: utf-8

# In[5]:


from collections import deque


# In[1]:


# Create a node class 
class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


# In[ ]:


class Tree:
    def __init__(self):
        # Initialise the root node with none
        self.root_node = None
    
    # Function to find the min node in the binary tree
    def min_node(self):
        current = self.root_node
        # Iterate over the left children of the each node to find the minimun node
        while current.left_child:
            current = current.left_child
        return current
    
    # Function to find the maximum node in the tree
    def max_node(self):
        current = self.root_node
        # Iterate over the right child of each children to node to find the maximum node
        while current.right_child:
            current = current.right_child
        return current
    
    # Function to insert the data
    def insert(self, data):
        node = Node(data)
        # Checking if there is any element present, if not make it the root node
        if not self.root_node:
            self.root_node = node
        # If there are other nodes present in the tree get the root node in the current and parent variables
        else:
            current = self.root_node
            parent = current
        while True:
            parent = current
            # If the to be inserted node's data attribute is greater than its parent go to right subtree
            if node.data > parent.data:
                current = current.right_child
                if not current:
                    parent.right_child = node
                    return
            # If the to be inserted node's data attribute is lesser than its parent go to left subtree
            else:
                current = current.left_child
                if not current:
                    parent.left_child = node
                    return
    # Helper function for the delete operation to get the node to be deleted along with its parent   
    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if not current:
            return (parent, current)
        while True:
            if current.data == data:
                return (parent, current)
            # If the data to be deleted is lesser than the parent iterate over the left subtree
            elif data < current.data:
                parent = current
                current = current.left_child
            # If the data to be deleted is greater than the parent then iterate over the right subtree
            else:
                parent = current
                current = current.right_child
        return (parent, current)
    
    # Function to delete a node in the tree  
    def delete(self, data):
        # Get the parent of the node to be deleted
        parent, current = self.get_node_with_parent(data)
        
        # If parend and the node is none then nothing is to be deleted
        if parent in None and current is None:
            return False
        children_count = 0
        
        # If the node to be deleted has both the left and right children then set the children_count variable to 2 
        if node.left_child and node.right_child:
            children_count = 2
            
        # If the node to be deleted has neither of left or right children then set the children_count variable to 0
        elif node.left_child is None and node.right_child is None:
            children_count = 0
            
        else:
            children_count = 1
            
        # If there is no children to node to be deleted
        if children_count == 0:
            if parent:
                # Check which child the node is to the parent make that reference none
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root_node = None
             
        # If there is only one child
        elif children_count == 1:
            next_node = None
            # Check which child the node has and assign it child to parent properly
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
         
        # If there are two children to the node to be deleted, find the in-order successor node and replace the node with it
        else:
            parent_of_left_most_node = node
            left_most_node = node.right_child
            # Iterate over the first by the right child and then the left children till finding the left most node
            while left_most_node.left_child:
                parent_of_left_most_node = left_most_node
                left_most_node = left_most_node.left_child
            node.data = left_most_node.data
            
            # If the in-order successor has a right child, make it left child of the in-order successor's parent
            if parent_of_left_most_node.left_child == left_most_node:
                parent_of_left_most_node.left_child = left_most_node.right_child
            # If the to be deleted node's right child is a leaf node    
            else:
                parent_of_left_most_node.right_child = left_most_node.right_child
            
    # Function to search for a particular data on the tree
    def search(self, data):
        current = self.root_node
        #Iterate over the tree untill the node is found
        while True:
            if not current:
                return None
            elif current.data == data:
                return True
            # If the data to be found is lesser than it parent, go left
            elif data < current.data:
                current = current.left_child
            # If the data to be found is greater than the parent, go right
            else:
                current = current.right_child
    
    # Function for inorder traversal to print in the order 'left child - current node - right child'
    def inorder_traversal(self):
        current = self.root_node
        if not current:
            return
        # Recursively run over the left child
        self.inorder_traversal(current.left_child)
        # Print the current node's data 
        print(current.data)
        # Recursively run over the right child
        self.inorder_traversal(current.right_child)
    
    # Function for preorder traversal to print out the data in the order  'current node - left child - right child'
    def preorder_traversal(self):
        current = self.root_node
        if not current:
            return
        # Print the current node's data 
        print(current.data)
        # Recursively run over the left child
        self.inorder_traversal(current.left_child)
        # Recursively run over the right child
        self.inorder_traversal(current.right_child)
        
    # Function for postorder traversal to print out the data in the order 'left child - right child - current child'
    def postorder_traversal(self):
        current = self.root_node
        if not current:
            return
        # Recursively run over the left child
        self.inorder_traversal(current.left_child)
        # Recursively run over the right child
        self.inorder_traversal(current.right_child)
        # Print the current node's data 
        print(current.data)


# In[ ]:




