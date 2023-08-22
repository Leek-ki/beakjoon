import sys

from collections import deque

M, N = map(int, sys.stdin.readline().split())

box = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

q = deque()
next_q = deque()
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            q.append((i, j))
# 상하좌우

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(box):
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))

bfs(box)

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()

print(max(map(max, box)) - 1)