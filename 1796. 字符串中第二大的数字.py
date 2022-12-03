class Solution:
    """
    1. 遍历字符串
    2. 如果是数字且没有重复：用插入排序（由小到大）将字符串转换为数组再输入到列表
    3. 返回列表的倒数第二的元素
    """

    def secondHighest(self, s: str) -> int:
        lst = []
        for i in range(len(s)):
            if s[i].isdigit():

                lst.append(int(s[i]))

                j = len(lst) - 1
                while len(lst) > 1 and j > 0:

                    # 如果重复：跳出循环
                    if lst[j] == lst[j - 1]:
                        lst.pop(j)
                        break

                    # 如果最后一个小于前一个：前移一位
                    if lst[j] < lst[j - 1]:
                        temp = lst[j]
                        lst[j] = lst[j - 1]
                        lst[j - 1] = temp
                    j = j - 1

        if len(lst) <= 1:
            return -1
        else:
            return lst[-2]


if __name__ == '__main__':
    s = Solution()
    res = s.secondHighest("dfa12321afd")
    print(res)
