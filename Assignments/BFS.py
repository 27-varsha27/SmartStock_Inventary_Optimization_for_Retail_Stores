from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Graph representation
graph = {
    0: [1, 2],
    1: [3],
    2: [4],
    3: [],
    4: []
}

bfs(graph, 0)
