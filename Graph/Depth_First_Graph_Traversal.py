#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import deque


# In[ ]:


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


# In[ ]:


# Function for depth first search traversal
def depth_first_search(root_node):
    # An empty list to note the visited nodes
    visited_nodes = []
    # List to hold nodes whose adjacent nodes to be visited next
    graph_stack = []
    graph_stack.append(root_node)
    node = root_node
    # Iterate over the stack list until it is empty
    while len(graph_stack) > 0:
        # If the node is not visited yet add it to the visited category
        if node not in visited_nodes:
            visited_nodes.append(node)
        # Get the adjacent nodes for the current node from the adjacecy list 
        adj_nodes = graph[node]
        # If all the adjacent nodes are currently visted pop the current node off the stack list
        if set(adj_nodes).issubset(set(visited_nodes)):
            graph_stack.pop()
            # If the stack list is not empty continue iteration
            if len(graph_stack) > 0:
                node = graph_stack[-1]
            continue
        else:
            # Find the adjacent nodes which are not yet visited
            remaining_nodes = set(adj_nodes).difference(set(visited_nodes))
        # Get the first node of sorted remaining nodes list
        first_adj_node = sorted(remaining_nodes)[0]
        # Append it to the stack list to be visited next
        graph_stack.append(first_adj_node)
        node = first_adj_node
    return visited_nodes

