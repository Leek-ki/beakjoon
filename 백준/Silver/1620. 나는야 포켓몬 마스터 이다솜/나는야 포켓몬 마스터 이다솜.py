import sys

N, M = map(int, input().split())

pocketmon = {}
pocketmon2 = {}

input = sys.stdin.readline

for i in range(1, N+1):
    name = input().rstrip()
    pocketmon[str(i)] = name
    pocketmon2[name] = str(i)

for i in range(1, M+1):
    quiz = input().rstrip()
    if quiz.isalpha():
        print(pocketmon2[quiz])
    else:
        print(pocketmon[quiz])