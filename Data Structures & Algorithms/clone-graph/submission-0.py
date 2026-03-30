"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        mapping = {}

        def dfs(node):
            if node == None:
                return None
            if node in mapping:
                return mapping[node]
            
            currNode = Node(node.val)
            mapping[node] = currNode


            for n in node.neighbors:
                # newNode = Node(n.val)
                currNode.neighbors.append(dfs(n))
                
            return currNode



        return dfs(node)

        