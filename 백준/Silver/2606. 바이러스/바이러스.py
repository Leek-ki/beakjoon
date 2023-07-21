com, pair = int(input()), int(input())
graph = [list(map(int, input().split())) for _ in range(pair)]
visited = [False] * (com + 1)
cnt = 0


def dfs(graph, v, visited):
    global cnt
    visited[v] = True
    for s, e in graph:
        if s == v and not visited[e]:
            cnt += 1
            dfs(graph, e, visited)
        elif e == v and not visited[s]:
            cnt += 1
            dfs(graph, s, visited)

dfs(graph, 1, visited)

print(cnt)