
def longest_sub_sequence(arr: list):
    """
    :param arr:
    :return: 每个数组下标对应值为结尾的最长子序列长度
    """
    # 全补1
    l = [1 for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                l[i] = max(l[j] + 1, l[i])
    return l


if __name__ == '__main__':
    arr11 = [3, 1, 4, 5, 6, 2, 1, 5, 7]
    res = longest_sub_sequence(arr11)
    print(res)
