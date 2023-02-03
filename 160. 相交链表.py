# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        '''
        如果两个链表相交 -> 相交节点的值相同
        相交节点的值相同 x> 两个链表相交
        '''

        p = headA
        q = headB

        arr1 = []
        arr2 = []

        while p or q:
            if p:
                arr1.append(p)
                p = p.next
            if q:
                arr2.append(q)
                q = q.next


        # 反向遍历数组

        arr1.reverse()
        arr2.reverse()

        pre = None

        i = 0
        j = 0

        # 两个数组的较小者的长度
        le = len(arr1) if len(arr1) < len(arr2) else len(arr2)

        if arr1[0] is not arr2[0]:
            return None

        while i < le and j < le:

            if arr1[i] is arr2[j]:
                pre = arr1[i]

            else:
                break

            i += 1
            j += 1

        return pre


if __name__ == '__main__':
    l1 = ListNode(4)
    # l2 = l1.next = ListNode(1)
    # l3 = l2.next = ListNode(8)
    # l4 = l3.next = ListNode(4)
    # l5 = l4.next = ListNode(5)

    i1 = ListNode(5)
    i2 = i1.next = ListNode(6)
    i3 = i2.next = ListNode(1)
    i4 = i3.next = ListNode(8)
    i5 = i4.next = ListNode(4)
    i6 = i5.next = ListNode(5)

    l1.next = i2.next

    s = Solution()
    c = s.getIntersectionNode(l1, i1)
    print(c.val)