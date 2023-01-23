# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 方法1：哈希表法
        # p = head
        #
        # flag = False
        #
        # if p is None:
        #     return flag
        #
        # dic = {}
        #
        # while p is not None:
        #     if dic.get(p.next):
        #         flag = True
        #         break
        #
        #     dic[p] = "1"
        #     p = p.next
        #
        # return flag

        # 方法2：快慢指针法： 如果存在环，两个指针一快一慢一定会在某一个时间相遇

        flag = False

        p = head
        if p is None:
            return flag

        q = p.next

        while p and q:
            if p is q:
                flag = True
                break

            p = p.next
            if not q.next:
                break
            q = q.next.next

        return flag


if __name__ == '__main__':
    l = ListNode(1)
    l2 = l.next = ListNode(2)
    l.next.next = l

    s = Solution()
    res = s.hasCycle(l)
    print(res)

