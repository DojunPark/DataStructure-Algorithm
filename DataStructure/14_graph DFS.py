# Depth First Search

RecursiveDFS(v):
    mark v as visited node
    for each edge (v, w):
        if w is unmarked:
            RecursiveDFS(w)

IterativeDFS(s):
    stack.push(s)
    while stack is not empty:
        v = stack.pop()
        if v is unmarked:
            mark v as visited node
            for each edge (v, w):
                if w is unmarked
                    stack.push(w)

DFS(v):
    mark v as visited node
    pre[v] = curr_time
    curr_time += 1
    for each edge(v, w):
        if w is unmarked:
            parent[w] = v
            DFS(w)
    post[v] = curr_time
    curr_time += 1

DFSALL(G):
    for all nodes v:
        unmark v
    for all nodes v:
        if v is unmarked:
            DFS(v)