def is_safe(node, color, graph, colors):
    for n in range(len(graph)):
        if graph[node][n] == 1 and colors[n] == color:
            return False
    return True

def branch_bound(graph, colors, m, node, best):
    if node == len(graph):
        used = len(set(colors))
        if used < best[0]:
            best[0] = used
            best[1] = colors[:]
        return
    for color in range(1, m+1):
        if is_safe(node, color, graph, colors):
            colors[node] = color
            if len(set(colors[:node+1])) < best[0]:
                branch_bound(graph, colors, m, node+1, best)
            colors[node] = 0

n = int(input("Enter number of nodes: "))
graph = []
print("Enter adjacency matrix:")
for _ in range(n):
    graph.append(list(map(int, input().split())))

m = int(input("Enter max number of colors: "))
colors = [0]*n
best = [m+1, []]

branch_bound(graph, colors, m, 0, best)

if best[1]:
    print("Optimal coloring:", best[1])
    print("Colors used:", best[0])
else:
    print("No solution")
