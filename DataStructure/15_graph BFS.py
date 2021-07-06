# Breadth First Search

BFS(G):
    visited = [False] * n
    parent = [-1] * n
    dist = [0] * n
    for all source node s in G:
        Q.enqueue(s)
        visited[s] = True
        while Q is not empty:
            v = Q.dequeue()
            for each edge v -> w:
                if not visited[w]:
                    Q.enqueue(w)
                    visited[w] = True
                    parent[w] = v
                    dist[w] = dist[v] + 1

