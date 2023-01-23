class Solution:
    def climbStairs(self, n: int) -> int:
        """
        可能排列的最大长度
                 最小长度
        例如 n=2
        max = 2 因为 11
        min = 1 ，， 2

        最大的长度 最小的长度的值都为1 介于两者之间的了能取值为当前可能取值的数
        例如 N = 5
        max = 5
        min = 3

        p_5 = 1
        p_4 = 4
        p_3 = 1
        p_sum = 6
        """

        max_ = n

        ji_shu = True if n % 2 else False

        if ji_shu:

            res = 1
            min_ = int(n / 2) + 1

            for i in range(min_, max_):
                res += i
        else:

            res = 2
            min_ = int(n / 2)

            for i in range(min_ + 1, max_):
                res += i

        return res


if __name__ == '__main__':
    o = Solution()
    t = o.climbStairs(4)
    print(t)
