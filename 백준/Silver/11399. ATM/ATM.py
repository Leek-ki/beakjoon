import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 0

for i in range(N+1):
    ans += sum(arr[:i])

print(ans)

