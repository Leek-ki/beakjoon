import sys

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

delta = [(0, 0), (0, 1), (1, 0), (1, 1)]

numofone = 0
numfozero = 0


def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[x][y] != arr[i][j]:
                return False
    return True

def bfs(x, y, n):
    if check(x, y, n):
        if arr[x][y] == 1:
            global numofone
            numofone += 1
        else:
            global numfozero
            numfozero += 1
        return
    else:
        for i in range(4):
            bfs(x + delta[i][0] * n // 2, y + delta[i][1] * n // 2, n // 2)

bfs(0, 0, n)

print(numfozero)
print(numofone)

