def dls_iterative(graph, start, goal, depth_limit):
    stack = [(start, 0)]  # (node, depth)

    while stack:
        node, depth = stack.pop()

        if node == goal:
            return True

        if depth < depth_limit:
            for neighbor in graph.get(node, []):
                stack.append((neighbor, depth + 1))

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

print(dls_iterative(graph, 'A', 'G', 3))  # True
