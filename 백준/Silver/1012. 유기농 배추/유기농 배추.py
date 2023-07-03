import sys
sys.setrecursionlimit(10000)
def dfs(x, y):
    dx = [-1, 1, 0, 0]  # 상하좌우
    dy = [0, 0, -1, 1]

    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if arr[x][y] == 1 and visited[x][y] == 0:
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    dfs(nx, ny)
        return True
    return False


cnt = int(input())

for _ in range(cnt):
    result = 0
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    visited = [[0] * N for _ in range(M)]
    for _ in range(K):
        x, y = map(int, input().split())
        arr[x][y] = 1
    for i in range(M):
        for j in range(N):
            if arr[i][j] == 1 and visited[i][j] == 0:
                if dfs(i, j):
                    result += 1
    print(result)
