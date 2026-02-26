

def bfs(G,v,n): # 그래프 G, 탐색 시작점 v...
    visited = [0]*(n+1)
    queue = []
    queue.append(v)
    visited[v]=1
    while queue:
        t = queue.pop(0)
        visit(t)
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1 

