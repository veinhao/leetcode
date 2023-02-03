# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 链表长度为0 OR 1
        if not head or not head.next:
            return head

        # 处理头节点
        p = head
        q = head.next
        n = q.next

        q.next = p
        p.next = None

        while True:
            p = q
            q = n
            if n:
                n = n.next
            else:
                break
            q.next = p

        return p

        # if not head:
#     return head
#
# arr = []
# p = head
#
# while p:
#     arr.append(p.val)
#     p = p.next
#
# arr.reverse()
#
# p = head
# i = 0
# while p:
#     p.val = arr[i]
#
#     i += 1
#     p = p.next
#
# return head

        # if not head:
        #     return head
        #
        # arr = []
        # p = head
        #
        # while p:
        #     arr.append(p.val)
        #     p = p.next
        #
        # arr.reverse()
        #
        # p = head
        # i = 0
        # while p:
        #     p.val = arr[i]
        #
        #     i += 1
        #     p = p.next
        #
        # return head


if __name__ == '__main__':
    i1 = ListNode(1)
    i2 = i1.next = ListNode(2)
    i3 = i2.next = ListNode(3)
    i4 = i3.next = ListNode(4)
    i5 = i4.next = ListNode(5)
    i6 = i5.next = ListNode(6)

    s = Solution()
    l = s.reverseList(i1)
    print(l)

