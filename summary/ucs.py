import heapq

def ucs(graph, start, goal):
    # Initialize the fringe (priority queue)
    fringe = []
    heapq.heappush(fringe, (0, start))  # Push the starting point with cost 0
    closed = set()  # Set of visited nodes
    best_cost = {start: 0}  # Dictionary to store the best cost to each node

    while fringe:
        # Get the node with the least cost
        cost, current = heapq.heappop(fringe)

        # If we have already visited this node, skip it
        if current in closed:
            continue

        # Mark the current node as visited
        closed.add(current)

        # If we've reached the goal, return success
        if current == goal:
            return 1  # Found the goal

        # Check neighbors of the current node
        for neighbor, neighbor_cost in graph[current]:
            # Skip if the neighbor has already been visited
            if neighbor in closed:
                continue

            # Calculate the new total cost to the neighbor
            total_cost = cost + neighbor_cost

            # If this is the best cost to reach the neighbor, update it
            if neighbor not in best_cost or total_cost < best_cost[neighbor]:
                best_cost[neighbor] = total_cost
                heapq.heappush(fringe, (total_cost, neighbor))  # Add the neighbor to the fringe

    # If no path is found, return failure
    return 0  # No path to the goal

# Example graph in adjacency list format
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)],
}

# Run UCS from 'A' to 'D'
result = ucs(graph, 'A', 'D')
print(result)  # Output: 1 (Goal found)
