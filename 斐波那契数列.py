
def fib(n):
    res = 0
    if n == 1 or n == 2:
        return 1
    elif n > 2:
        #   5
        # 4   3
        # 3  2 2  1

        # 1 1 2 3 5 8 13 21

        res = fib(n-1) + fib(n-2)
    return res


def fib2(n, arr: list):
    res = 0
    if arr[n] != -1:
        return arr[n]
    if n == 1 or n == 2:
        return 1
    if n > 2:
        res = fib2(n-1, arr) + fib2(n-2, arr)
        arr[n] = res
    return res


if __name__ == '__main__':
    ress = fib2(8, arr=[-1 for i in range(50)])
    print(ress)
