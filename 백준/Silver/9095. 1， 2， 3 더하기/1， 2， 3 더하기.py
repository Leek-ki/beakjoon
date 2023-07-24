# 순열, 조합
import sys

input = sys.stdin.readline

N = int(input())
cnt = 0


def sol(M):
    global cnt
    if M == 0:
        cnt = cnt + 1
        return cnt
    else:
        if M - 1 >= 0:
            sol(M - 1)
        if M - 2 >= 0:
            sol(M - 2)
        if M - 3 >= 0:
            sol(M - 3)

    return cnt


for _ in range(N):
    M = int(input())
    print(sol(M))
    cnt = 0
