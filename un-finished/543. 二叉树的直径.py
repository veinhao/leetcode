from typing import Optional
from tool.generate_t import generate_tree
from tool.generate_t import TreeNode


# 二叉树的直径 = 二叉树的各个叶子节距离的最大值
# 也就是从某一个根节点出发左右两边经过节点之和


class Solution:
    def __init__(self):
        self.res = 0

    def a(self, root) -> int:
        if not root:
            return 0

        L = self.a(root.left)
        R = self.a(root.right)

        self.res = L + R if L + R > self.res else self.res

        return max(L, R) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.a(root)

        return self.res


if __name__ == '__main__':
    s = Solution()
    null = None
    t = generate_tree(
        [1, 2, 3, 4, 5, 6, 7, null, 9, 0])

    y = s.diameterOfBinaryTree(t)
    print(y)
