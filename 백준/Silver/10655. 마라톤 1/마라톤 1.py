import sys

N = int(input())

coor_list = dict()

for i in range(N):
    coor_list[i] = tuple(map(int, sys.stdin.readline().split()))

origin_distance = 0
ans = -5000
for i in range(N - 1):
    origin_distance += abs(coor_list[i][0] - coor_list[i + 1][0]) + abs(coor_list[i][1] - coor_list[i + 1][1])

for i in range(1, N - 1):
    ab = abs(coor_list[i][0] - coor_list[i + 1][0]) + abs(coor_list[i][1] - coor_list[i + 1][1]) + abs(
        coor_list[i][0] - coor_list[i - 1][0]) + abs(coor_list[i][1] - coor_list[i - 1][1])
    aa = abs(coor_list[i-1][0] - coor_list[i + 1][0]) + abs(coor_list[i-1][1] - coor_list[i + 1][1])
    if ab-aa>ans:
        ans = ab-aa

print(origin_distance-ans)