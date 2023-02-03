
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            # 两者都为空
            if not p and not q:
                return True
            # 只有一个为空
            return False

        root = False

        # 值不相等，一定错，值相等不一定对
        if p.val != q.val:
            return False
        else:
            root = True

        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right and root
