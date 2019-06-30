#!/usr/bin/env python
# coding: utf-8

# In[3]:


from collections import deque


# In[2]:


# Create the graph adjacency list
graph = dict()
graph['A'] = ['C', 'E']
graph['B'] = ['D', 'E', 'F']
graph['C'] = ['A', 'F']
graph['D'] = ['B', 'H', 'G']
graph['E'] = ['A', 'B', 'H']
graph['F'] = ['B', 'C']
graph['G'] = ['D']
graph['H'] = ['D', 'E']


# In[5]:


# Function for breadth first search traversal
def breadth_first_search(root_node):
    # Initialize an empty list to note the visited nodes
    visited_nodes = []
    # Create a deque object to hold the nodes to be visited next
    graph_queue = deque([root_node])
    visited_nodes.append(root_node)
    node = root_node
    # Iterate until all the nodes are visited
    while len(graph_queue) > 0:
        # Pop node from the graph queue
        node = graph_queue.popleft()
        # Find the adjacent nodes of the current node using the adjacency list
        adj_nodes = graph[node]
        # Get the adjacent nodes which are yet to be visited 
        remaining_nodes = set(adj_nodes).difference(set(visited_nodes))
        # If there are any adjacent nodes to be visited
        if len(remaining_nodes) > 0:
            # Sort and iterate over the nodes
            for i in sorted(remaining_nodes):
                # Add these nodes those to visited nodes
                visited_nodes.append(i)
                # Add these nodes for visiting their adjacent nodes
                graph_queue.append(i)
    return visited_nodes


# In[ ]:




