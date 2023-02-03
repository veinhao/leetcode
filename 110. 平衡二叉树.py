# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # 当前深度
        self.cur = 0

    def zone(self, root: Optional[TreeNode]) -> int:
        if not root:
            return self.cur

        # 比较左边最大的深度和右边最大的深度

        self.cur += 1
        left = self.zone(root.left)
        right = self.zone(root.right)
        self.cur -= 1

        if left == -1 or right == -1:
            return -1

        if abs(left - right) >= 2:
            return -1

        return left if left > right else right

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return False if self.zone(root) == -1 else True

