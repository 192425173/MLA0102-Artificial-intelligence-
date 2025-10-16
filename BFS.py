from collections import deque

def bfs(graph, start):
    visited = set()          
    queue = deque([start])   
    order = []               

    while queue:
        node = queue.popleft()    
        if node not in visited:
            visited.add(node)     
            order.append(node)    
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return order

# Example Graph as Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start BFS from node 'A'
bfs_order = bfs(graph, 'A')
print("BFS Traversal Order:",bfs_order)