# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max = 0
        self.i = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.i += 1
        self.max = self.i if self.i > self.max else self.max

        self.maxDepth(root.left)

        self.maxDepth(root.right)
        self.i -= 1

        return self.max


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(3)

    t.left = TreeNode(9)
    t.right = TreeNode(20)
    t.right.left = TreeNode(15)
    t.right.right = TreeNode(7)

    o = s.maxDepth(t)
    print(o)
