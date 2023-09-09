import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
mapmap = list()

for i in range(n):
    mapp = list(map(int, input().split()))
    mapmap.append(mapp)
    if 2 in mapp:
        goal = (i, mapp.index(2))

q = deque()
ansmap = list(list(0 for i in range(m)) for j in range(n))

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ansmap[goal[0]][goal[1]] = 0

for dd in d:
    dx, dy = dd[0], dd[1]
    nx, ny = goal[0] + dx, goal[1] + dy
    if n > nx >= 0 and m > ny >= 0 and mapmap[nx][ny] != 0:
        q.append((nx, ny))
        ansmap[nx][ny] = 1

while q:
    x, y = q.popleft()
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if n > nx >= 0 and m > ny >= 0 and mapmap[nx][ny] != 0:
            if ansmap[nx][ny] == 0:
                q.append((nx, ny))
                ansmap[nx][ny] = ansmap[x][y] + 1
            elif ansmap[nx][ny] > ansmap[x][y] + 1:
                q.append((nx, ny))
                ansmap[nx][ny] = ansmap[x][y] + 1

ansmap[goal[0]][goal[1]] = 0

for i in range(n):
    for j in range(m):
        if mapmap[i][j] == 1 and ansmap[i][j] == 0:
            ansmap[i][j] = -1

for i in ansmap:
    print(*i)
