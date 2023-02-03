class Solution:
    def plusOne(self, digits: list) -> list:
        # n = len(digits)
        # num = 0
        # for i in range(n):
        #     num += digits[n - 1 - i] * 10 ** i
        #
        # num += 1
        # n = len(str(num))
        #
        # # 999
        # res = []
        # for i in range(n):
        #     res.append(int(num / (10 ** (n - i - 1))))
        #     num = num % (10 ** (n - i - 1))
        #
        # return res

        res = []

        # 只会在一种情况下扩容，就是全是9
        only9 = False
        i = len(digits) - 1
        while i >= 0:

            if i == 0 and digits[i] == 9:
                only9 = True

            if digits[i] != 9:
                only9 = False
                break
            i -= 1

        i = len(digits) - 1
        if only9:
            res.append(1)
            for i in range(i + 1):
                res.append(0)
            return res


        for j in range(i+1):
            jinwei = 1 if digits[i - j] == 9 else 0
            if jinwei:
                digits[i - j] = 0
            else:
                digits[i - j] += 1
                break

        return  digits



if __name__ == '__main__':
    s = Solution()
    l = s.plusOne([9])
    print(l)
