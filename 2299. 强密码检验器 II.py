class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        '''
        将条件划为5个Flase
        循环遍历password
        如果某个条件不满足：退出
        '''
        flag1 = False  # 至少包含 一个小写英文 字母。
        flag2 = False  # 至至少包含 一个大写英文 字母。
        flag3 = False  # 至少包含 一个数字 。
        flag4 = False  # 至少包含 一个特殊字符 。特殊字符为："!@#$%^&*()-+" 中的一个。
        flag5 = False  # 不包含 2个连续相同的字符。

        pre_i = ""
        for i in range(len(password)):
            if password[i].islower():
                flag1 = True
            if password[i].isupper():
                flag2 = True
            if password[i].isdigit():
                flag3 = True
            if password[i] in "!@#$%^&*()-+":
                flag4 = True
            if i != 0 and pre_i == password[i]:
                flag5 = True

            pre_i = password[i]

        if flag1 and flag2 and flag3 and flag4 and not flag5:
            return True
        else:
            return False


if __name__ == '__main__':
    o = Solution()
    res = o.strongPasswordCheckerII("IloveLe3tcode!")
    print(res)

