class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        i = len(nums) - 1

        start = 0
        end = i

        i = int(i / 2)

        store_i = 0

        while start <= end:

            if nums[i] == target:
                store_i = i
                break

            elif nums[i] < target:
                start = i + 1

            else:
                end = i - 1

            i = int((end + start) / 2)

        # 没找到
        if start > end:
            store_i = start

        return store_i



