# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from tool.generate_t import generate_tree, TreeNode


class Solution:
    def __init__(self):
        self.cur = 0
        self.min = 10000

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.cur += 1
        if not root.left and not root.right:
            if self.cur < self.min:
                self.min = self.cur
        self.minDepth(root.left)
        self.minDepth(root.right)
        self.cur -= 1

        return self.min

        # 方法一
        # if not root:
        #     return
        #
        # self.cur += 1
        #
        # # 叶子节点
        # if not root.left and not root.right:
        #     # 当前深度大于最小深度，没有必要继续更新；否则更新最小深度
        #     if self.cur > self.min:
        #         self.cur -= 1
        #         return self.min
        #     self.min = self.cur
        #
        # self.minDepth(root.left)
        # self.minDepth(root.right)
        #
        # self.cur -= 1
        #
        # return self.min


if __name__ == '__main__':
    s = Solution()
    root = generate_tree([3, 4, 5, -7, -6, None, None, -7, None, -5, None, None, None, -4])
    l = s.minDepth(root)
    print(l)
