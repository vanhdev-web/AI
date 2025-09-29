import heapq

def a_star(graph, start, goal, heuristic):
    # priority queue: (f(n), g(n), node, path)
    frontier = [(heuristic[start], 0, start, [start])]
    explored = {}

    while frontier:
        f, g, node, path = heapq.heappop(frontier)

        if node == goal:
            return path, g  # trả về đường đi và chi phí

        if node in explored and explored[node] <= g:
            continue
        explored[node] = g

        for neighbor, cost in graph.get(node, []):
            new_g = g + cost
            new_f = new_g + heuristic[neighbor]
            heapq.heappush(frontier, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float("inf")


# ví dụ đồ thị có cost
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [],
    'E': [('F', 3)],
    'F': []
}

# heuristic: khoảng cách ước lượng từ node đến goal 'F'
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 12,
    'E': 2,
    'F': 0
}

path, cost = a_star(graph, 'A', 'F', heuristic)
print("Đường đi:", path)
print("Chi phí:", cost)
