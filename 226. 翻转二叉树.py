# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.arr = []

        self.count = 0

    def mid(self, root: Optional[TreeNode]):
        if root is None:
            return

        self.mid(root.left)
        self.arr.append(root.val)
        self.mid(root.right)

    def mid2(self, root: Optional[TreeNode]):
        if root is None:
            return

        self.mid2(root.left)
        root.val = self.arr[self.count]
        self.count += 1
        self.mid2(root.right)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.mid(root)
        self.arr.reverse()
        self.mid2(root)

        return root


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(2)

    t.right = TreeNode(3)

    t.left = TreeNode(1)

    # t.left.left = TreeNode(4)

    # t.left.right = TreeNode(67)

    # t.left.right.left = TreeNode(8)

    # t.left.right.right = TreeNode(-97)
    #
    # t.right.left = TreeNode(67)

    # t.right.right = TreeNode(4)

    # t.right.left.left = TreeNode(-97)

    # t.right.right.left = TreeNode(9)
    #
    # t.right.right.right = TreeNode(8)

    y = s.invertTree(t)
    print(y)
