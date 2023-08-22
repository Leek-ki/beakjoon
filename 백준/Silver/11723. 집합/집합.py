import sys

input = sys.stdin.readline

S = 0
for _ in range(int(input())):
    cmd = input().split()
    if cmd[0] == "add":
        M = 1 << (int(cmd[1]) - 1)
        S = S | M
    elif cmd[0] == "remove":
        M = 1 << (int(cmd[1]) - 1)
        S = S & ~M
    elif cmd[0] == "check":
        M = 1 << (int(cmd[1]) - 1)
        if S & M:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        M = 1 << (int(cmd[1]) - 1)
        S = S ^ M
    elif cmd[0] == "all":
        S = 2 ** 20 - 1
    elif cmd[0] == "empty":
        S = 0
