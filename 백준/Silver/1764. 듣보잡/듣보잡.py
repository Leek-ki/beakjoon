N,M = map(int, input().split())

D = [input() for _ in range(N)]
B = [input() for _ in range(M)]
DB = list(set(D) & set(B))

print(len(DB))
for i in sorted(DB):
    print(i)


