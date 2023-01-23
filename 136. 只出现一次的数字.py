class Solution:
    def singleNumber(self, nums) -> int:

        # if len(nums) == 1:
        #     return nums[0]
        #
        # dic = {}
        # res = -1
        #
        # for i in nums:
        #     if dic.get(i):
        #         dic[i] = False
        #     else:
        #         dic[i] = True
        #
        # for i in dic:
        #     if dic[i]:
        #         res = i
        #
        # return res

        # 方法二：异或
        # 交换律：A ^ B ^ A == A ^ A ^B
        # 结合律 ( A ^ B ) ^ C = A ^ ( B ^ C )
        # 两个相同的数异或为0 : 0 ^ 0 = 0
        # 0 ^ 任何数 == 任何数

        # python 异或会先将不同的加起来，如果后面有相同的，那么减去相同的值，得出的结果就是最终的
        res = nums[0]

        for i in nums[1:]:
            res = res ^ i

        return res


if __name__ == '__main__':
    s = Solution()
    o = s.singleNumber([4,1,2,1,2])
    print(o)