def dls(graph, start, goal, depth_limit):
    stack = [(start, 0)]  # (node, depth)

    while stack:
        node, depth = stack.pop()

        if node == goal:
            return True

        if depth < depth_limit:
            for neighbor in graph.get(node, []):
                stack.append((neighbor, depth + 1))

    return False


def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):  # tăng dần độ sâu
        if dls(graph, start, goal, depth):
            return True
    return False


# ví dụ đồ thị
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}

print(ids(graph, 'A', 'G', 3))  # True
