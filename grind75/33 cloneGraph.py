
# Definition for a Node.
from collections import defaultdict


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        visited={}

        def dfs(node):
            if not node:
                return
            copyOfNode = Node(node.val)
            visited[node]=copyOfNode
            for n in node.neighbors:
                if n in visited:
                    copyOfNode.neighbors.append(visited[n])
                else:
                    copyOfNode.neighbors.append(dfs(n))
            return copyOfNode

        return dfs(node)
            