class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''
        记录所有0的下标
        1 0 1 0 2
        第一个0后面的数字只需要统一向前移动一步
        第二个0 移动两步
        。。。

        如果只有0 or 没有0：不需要操作
        '''

        # 记录0的位置
        # arr_z = []
        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         arr_z.append(i)
        #
        # if len(arr_z) == 0 or len(arr_z) == len(nums):
        #     return
        #
        # count = 0
        #
        # for j in range(len(arr_z)):
        #     count += 1
        #     if j == len(arr_z) - 1:
        #         for i in range(arr_z[j] + 1, len(nums)):
        #             nums[i - count] = nums[i]
        #
        #     else:
        #         for i in range(arr_z[j] + 1, arr_z[j + 1]):
        #             nums[i - count] = nums[i]
        #
        # # 给后面补零
        # for j in range(1, len(arr_z) + 1):
        #     nums[-j] = 0


if __name__ == '__main__':
    s = Solution()

    l = [1, 0, 2, 0, 3]

    s.moveZeroes(l)

    print(l)

