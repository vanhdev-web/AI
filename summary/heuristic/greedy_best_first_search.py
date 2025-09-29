import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    # priority queue: (h(n), node, path)
    frontier = [(heuristic[start], start, [start])]
    explored = set()

    while frontier:
        _, node, path = heapq.heappop(frontier)

        if node == goal:
            return path

        if node in explored:
            continue
        explored.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in explored:
                heapq.heappush(frontier, (heuristic[neighbor], neighbor, path + [neighbor]))

    return None


# ví dụ đồ thị
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# heuristic: khoảng cách ước lượng đến goal 'F'
heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 4,
    'E': 2,
    'F': 0
}

path = greedy_best_first_search(graph, 'A', 'F', heuristic)
print("Đường đi:", path)
