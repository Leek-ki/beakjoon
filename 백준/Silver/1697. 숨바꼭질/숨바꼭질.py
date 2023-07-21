from collections import deque

cur, end = map(int, input().split())




def bfs(cur, end):
    sett = set()
    queue = deque()
    queue.append([cur, 0])

    while queue:
        cur, cnt = queue.popleft()
        sett.add(cur)
        if cur == end:
            return cnt
        else:
            if cur * 2 <= 100000 and cur * 2 not in sett:
                queue.append([cur * 2, cnt + 1])
            if cur + 1 <= 100000 and cur + 1 not in sett:
                queue.append([cur + 1, cnt + 1])
            if cur - 1 >= 0 and cur - 1 not in sett:
                queue.append([cur - 1, cnt + 1])

        # 못 찾았을 경우
    return -1


print(bfs(cur, end))
