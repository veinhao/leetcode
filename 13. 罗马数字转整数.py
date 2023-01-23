class Solution:
    def romanToInt(self, s: str) -> int:
        """
        顺序读取罗马数字
        如果当前读取的字符为 I X C: 取下一位（保证当前不是最后一位）字符
            判断两位字符是否对应IV IX XL...（这些字符被保存在字典中）
        """

        dic = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        dic2 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        tmp_skip = False
        for i in range(len(s)):
            # 如果跳过这次循环
            if tmp_skip:
                tmp_skip = False
                continue
            # 特殊情况
            if i != len(s) and s[i:i+2] in dic:
                tmp_skip = True
                res += dic.get(s[i:i+2])
            # 一般情况
            elif s[i] in dic2:
                res += dic2.get(s[i])

        return res


if __name__ == '__main__':

    o = Solution()
