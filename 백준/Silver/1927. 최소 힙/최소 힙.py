import heapq
import sys

heap = []


def insert(num):
    heapq.heappush(heap, num)


def delete():
    if len(heap) == 0:
        return 0
    else:
        return heapq.heappop(heap)


input = sys.stdin.readline

for _ in range(int(input())):
    input_if = int(input())
    if input_if == 0:
        print(delete())
    else:
        insert(input_if)
