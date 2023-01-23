# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self, lst=[]):
        self.array = []

        # r = TreeNode()
        # r.val = lst[0]
        #
        # self.t = [r]
        #
        # j = 1
        #
        # for i in range(len(self.t)):
        #
        #     p_j = j
        #
        #     self.t[i].left = TreeNode()
        #     self.t[i].left.val = lst[j]
        #     j += 1
        #
        #     self.t[i].right = TreeNode()
        #     self.t[i].right.val = lst[j]
        #     j += 1
        #
        #     # 给数组赋值
        #     for k in range(p_j, 2*len(self.t) + 1):
        #         self.t.clear()
        #         self.t.append(k)

    def access(self, array: list) -> bool:
        i = 0
        j = len(array) - 1
        flag = True
        while i < j:
            if array[i] is not array[j]:
                flag = False
                break

            i += 1
            j -= 1

        return flag

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        '''
        1 2 4 8 ...
        每层有节点：2**(n-1)
        从每层的开始和结尾向中间遍历

        n 2 3 1 3 2 n
        '''

        # if root is None:
        #     self.array.append(None)
        #     return
        #
        # # 当前节点是叶子节点
        # if root.left is None and root.right is None and root is not None:
        #     self.array.append(root.val)
        #     return
        #
        # self.isSymmetric(root.left)
        # self.array.append(root.val)
        # self.isSymmetric(root.right)
        #
        # return self.access(self.array)
        flag = True
        # 装载每一层的值
        pre_array = [root]
        while pre_array:
            p_array = []
            for i in pre_array:

                # if i.left is not None or i.right is not None:
                #     p_array.append(i.left)
                #     p_array.append(i.right)

                if i.left is None:
                    self.array.append(-101)
                    # if i.right is not None:
                    #     self.array.append(-101)
                else:
                    p_array.append(i.left)
                    self.array.append(i.left.val)

                if i.right is None:
                    # if i.left is not
                    self.array.append(-101)

                else:
                    p_array.append(i.right)
                    self.array.append(i.right.val)

            if not self.access(self.array):
                flag = False
                break

            self.array.clear()

            pre_array = p_array

        return flag


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(4)

    t.right = TreeNode(-57)

    t.left = TreeNode(-57)

    # t.left.left = TreeNode(4)

    t.left.right = TreeNode(67)

    # t.left.right.left = TreeNode(8)

    t.left.right.right = TreeNode(-97)

    t.right.left = TreeNode(67)

    # t.right.right = TreeNode(4)

    t.right.left.left = TreeNode(-97)

    # t.right.right.left = TreeNode(9)
    #
    # t.right.right.right = TreeNode(8)

    y = s.isSymmetric(t)
    print(y)
