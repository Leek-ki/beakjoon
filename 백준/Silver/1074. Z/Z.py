N, r, c = map(int, input().split())


def Z(n, x, y):
    if n == 1:
        return 2 * x + y

    # 1
    if x < 2 ** (n - 1) and y < 2 ** (n - 1):
        return Z(n - 1, x, y)
    # 2
    elif x < 2 ** (n - 1) <= y:
        return Z(n - 1, x, y - 2 ** (n - 1)) + 4 ** (n - 1)
    # 3
    elif x >= 2 ** (n - 1) > y:
        return Z(n - 1, x - 2 ** (n - 1), y) + 2 * 4 ** (n - 1)
    # 4
    else:
        return Z(n - 1, x - 2 ** (n - 1), y - 2 ** (n - 1)) + 3 * 4 ** (n - 1)


print(Z(N, r, c))
