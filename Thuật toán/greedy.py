

def greedy(graph, start, end):
    fringe = []
    closed = []

    fringe.append((start, 0))

    while fringe:
        current = fringe[0]
        for i in fringe:
            if i[1] < current[1]:
                current = i
        fringe.remove(current)
        closed.append(current)

        if current[0] == end:
            return closed

        neighbors = graph[current[0]]

        for i in neighbors:
            if i in closed or i in fringe:
                continue
            else :
                fringe.append(i)
    return closed


graph = {
    'S': [('A', 3), ('B', 4)],
    'A': [('B', 4), ('C', 2), ('D', 2), ('G', 0)],
    'B': [('C', 2)],
    'C': [('G', 0)],
    'D': [('G', 0)],
    'G': []
}
print("start")
result = greedy(graph, 'S', 'G')
print(result)
print("end")