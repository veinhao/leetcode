class Solution:
    def mySqrt(self, x: int) -> int:
        # i = 0
        # res = i
        # while True:
        #     if i*i <= x and (i + 1)*(i + 1) > x:
        #         res = i
        #         break
        #     i += 1
        # return res

        # 牛顿法 y = x2, y` = 2x
        xn1 = 0
        xn = 1
        for i in range(50):
            xn1 = xn - (xn*xn - x) / (2 * xn)
            xn = xn1

        return xn1




if __name__ == '__main__':
    s = Solution()
    l = s.mySqrt(2147395599)
    print(l)