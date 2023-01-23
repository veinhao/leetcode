# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 定义栈
class stack:
    def __init__(self):
        self.elems = []

    def add(self, val):
        self.elems.append(val)

    def pop(self):
        res = self.elems.pop()
        return res

    def top(self):
        return self.elems[-1]


class Solution:
    def __init__(self):
        self.array = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> list:
        """
        optional 除了可以取默认值还可以取None
        """

        # if root == None:
        #     return
        # # 访问左节点
        # self.inorderTraversal(root.left)
        # # 访问当前节点
        # self.array.append(root.val)
        # # 访问右节点
        # self.inorderTraversal(root.right)

        """
        for循环中序遍历二叉树
        """
        s = stack()
        p = root
        if not root:
            return []

        s.add(p)

        while s.elems:

            # 节点左边不为空，继续访问左边
            while p.left:
                s.add(p.left)
                p = p.left

            # 左节点为空
            # 加入结果集
            self.array.append(s.pop().val)

            # 右节点有值
            if p.right:
                s.add(p.right)
                p = p.right

            # 右节点没有值
            else:
                x = s.pop()
                self.array.append(x.val)
                p = x.right

        return self.array


if __name__ == '__main__':
    s = Solution()
    t = TreeNode()
    t.val = 1

    t.right = TreeNode()
    t.right.val = 2

    t.right.left = TreeNode()
    t.right.left.val = 3

    y = s.inorderTraversal([1])
