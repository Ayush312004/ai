def is_safe(node, color, graph, colors):
    for neighbor in range(len(graph)):
        if graph[node][neighbor] == 1 and colors[neighbor] == color:
            return False
    return True

def graph_coloring(node, graph, m, colors):
    if node == len(graph):
        return True
    for color in range(1, m+1):
        if is_safe(node, color, graph, colors):
            colors[node] = color
            if graph_coloring(node+1, graph, m, colors):
                return True
            colors[node] = 0
    return False

n = int(input("Enter number of nodes: "))
graph = []
print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter number of colors: "))
colors = [0] * n

if graph_coloring(0, graph, m, colors):
    print("Colors assigned:", colors)
else:
    print("No solution possible")
