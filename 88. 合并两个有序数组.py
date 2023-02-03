class Solution:
    def merge(self, nums1: list, nums2: list) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if not nums2:
            return nums1

        res = []

        p = q = 0
        while True:

            if nums1[p] == 0 and q >= len(nums2):
                break
            if nums1[p] == 0:
                res.append(nums2[q])
                q += 1
                continue
            if q >= len(nums2):
                res.append(nums1[p])
                p += 1
                continue

            if nums1[p] == nums2[q]:
                res.append(nums1[p])
                res.append(nums1[p])
                p += 1
                q += 1
            elif nums1[p] < nums2[q]:
                res.append(nums1[p])
                p += 1
            elif nums2[q] < nums1[p]:
                res.append(nums2[q])
                q += 1

        for i in range(len(res)):
            nums1[i] = res[i]


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3, 4, 5, 6, 7, 0, 0, 0]
    nums2 = [3, 4, 5]
    s.merge(nums1, nums2)
    print(nums1)
