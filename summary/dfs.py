from collections import deque

def dfs (graph, start, goal):
    fringe = deque()
    closed = set()

    fringe.append(start)

    while fringe:
        current = fringe.pop()
        closed.add(current)
        if current == goal:
            return 1
        neighbors = graph[current]
        for item in neighbors:
            if (item not in fringe ) and (item not in closed):
                fringe.append(item)
    return 0

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    result = dfs(graph,start= "A", goal = "F")
    print(result)


