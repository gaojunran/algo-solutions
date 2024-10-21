from typing import Optional

from linked_list.ListNode import ListNode

"""
Solution1: Iterative Solution
双指针法。
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            tmp = curr.next
            curr.next = prev
            # 注意此时链表已经反转，要通过tmp而不是curr.next来更新curr
            prev = curr
            curr = tmp
            # also available: cur.next, pre, cur = pre, cur, cur.next
        return prev


