# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        flag = True

        p = head
        arr = []
        while p:
            arr.append(p.val)
            p = p.next

        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i] != arr[j]:
                flag = False
                break

            i += 1
            j -= 1
        return flag



if __name__ == '__main__':
    l = ListNode(1)
    l.next = ListNode(2)

    l.next.next = ListNode(2)
    l.next.next.next = ListNode(1)

    s = Solution()
    t = s.isPalindrome(l)
    print(t)
