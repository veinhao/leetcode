class Solution:

    def __init__(self):
        self.lst = '0'

    # 参数：二进制字符串， 起初1的数目
    def b_plus(self, orig_1) -> int:
        o = orig_1
        n = len(self.lst) - 1
        self.lst = list(self.lst)
        for i in range(len(self.lst)):
            if n - i == 0:
                if self.lst[n - i] == '1':
                    self.lst[n - i] = '10'

                if self.lst[n - i] == '0':
                    o += 1
                    self.lst[n - i] = '1'

            else:
                if self.lst[n - i] == '1':
                    o -= 1
                    self.lst[n - i] = '0'
                if self.lst[n - i] == '0':
                    o += 1
                    break

        self.lst = ''.join(self.lst)
        return o

    def countBits(self, n: int) -> list:
        # ans = [0]
        # for i in range(1, n + 1):
        #     count = 0
        #     while i:
        #         i /= 2
        #         if i % 1 != 0.0:
        #             count += 1
        #         i = int(i)
        #
        #     ans.append(count)
        # return ans

        ans = [0]
        orig_1 = 0

        for i in range(n + 1):

            ans.append(self.b_plus(orig_1))

        return ans

if __name__ == '__main__':
    s = Solution()
    l = s.countBits(4)
    print(l)
