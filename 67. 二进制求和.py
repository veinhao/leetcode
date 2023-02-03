class Solution:
    def addBinary(self, a: str, b: str) -> str:

        i = len(a) - 1
        j = len(b) - 1
        res = ''
        jinwei = 0
        while i != -1 or j != -1:
            # 两者都有值
            if i != -1 and j != -1:
                # 0 1
                if a[i] != b[j] and jinwei:
                    res += str(0)
                    jinwei = 1
                elif a[i] != b[j] and not jinwei:
                    res += str(1 + jinwei)
                    jinwei = 0
                else:
                    # 1 1
                    if a[i] == '1':
                        res += str(0 + jinwei)
                        jinwei = 1
                    else:
                        res += str(0 + jinwei)
                        jinwei = 0

                i -= 1
                j -= 1

            # 有一个有值
            elif i == -1:
                if b[j] != str(jinwei):
                    res += str(1)
                    jinwei = 0
                elif b[j] == str(jinwei):
                    if b[j] == '0':
                        res += '0'
                    else:
                        res += '0'
                        jinwei = 1
                j -= 1
            elif j == -1:
                if a[i] != str(jinwei):
                    res += str(1)
                    jinwei = 0
                elif a[i] == str(jinwei):
                    if a[i] == '0':
                        res += '0'
                    else:
                        res += '0'
                        jinwei = 1
                i -= 1

        if jinwei:
            res += str(1)

        # b = ''
        # for i in range(len(res)):
        #     b += res[len(res) - 1 - i]

        return res[::-1]


if __name__ == '__main__':
    s = Solution()
    l = s.addBinary("110010", "10111")
    print(l)
