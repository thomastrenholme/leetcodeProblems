# traverse using bfs printing at each stage
def bfs(start):
    # create a queue
    queue = []
    # create a set to store visited nodes
    visited = set()
    # add the start node to the queue
    queue.append(start)
    # while the queue is not empty
    while queue:
        # pop the first node from the queue
        node = queue.pop(0)
        # if the node is not visited
        if node not in visited:
            # print the node
            print(node)
            # add the node to the visited set
            visited.add(node)
            # add the neighbors of the node to the queue
            for neighbor in node.neighbors:
                queue.append(neighbor)


# traverse using dfs printing at each stage
def dfs(start):
    # create a stack
    stack = []
    # create a set to store visited nodes
    visited = set()
    # add the start node to the stack
    stack.append(start)
    # while the stack is not empty
    while stack:
        # pop the first node from the stack
        node = stack.pop()
        # if the node is not visited
        if node not in visited:
            # print the node
            print(node)
            # add the node to the visited set
            visited.add(node)
            # add the neighbors of the node to the stack
            for neighbor in node.neighbors:
                stack.append(neighbor)