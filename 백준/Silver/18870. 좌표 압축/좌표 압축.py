import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
coordinate_arr = list(map(int, input().split()))
answer_arr = list()

sorted_coordinate_arr = sorted(set(coordinate_arr))

index_dict = {val: idx for idx, val in enumerate(sorted_coordinate_arr)}

for i in coordinate_arr:
    answer_arr.append(index_dict[i])

print(*answer_arr)
