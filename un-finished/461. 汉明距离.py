class Solution:

    def to2(self, n: int) -> str:
        '4 : 100'

        res = ''

        while n:
            n = n / 2
            if n % 1 == 0.0:
                res = '0' + res
            else:
                res = '1' + res

            n = int(n)
        return res

    def hammingDistance(self, x: int, y: int) -> int:

        if x == y:
            return 0

        count = 0
        x1 = self.to2(x)
        x2 = self.to2(y)

        l1 = len(x1)
        l2 = len(x2)

        if l1 != l2:
            if l1 > l2:
                sub = l1 - l2
                for i in range(sub):
                    x2 = '0' + x2

            else:
                sub = l2 - l1
                for i in range(sub):
                    x1 = '0' + x1

        for i in range(len(x1)):
            if x1[i] != x2[i]:
                count += 1

        return count

        # better way
