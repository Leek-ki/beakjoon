import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)


def sol(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    if N == 2:
        return 2
    else:
        dp[1] = 1
        dp[2] = 2
        for i in range(3, N + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[N]

print(int(sol(N) % 10007))
