"""
Solution1: Double Pointers
使用快慢指针法，快指针每次移动两步，慢指针每次移动一步，
如果存在环，则快指针会追上慢指针（因为快指针会一直在环里移动）。
思考：为什么不能快指针每次移动三步？
"""
from linked_list.ListNode import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


# class Solution2:
#     def hasCycle(self, head: ListNode) -> bool:
#         if not head or not head.next:
#             return False
#         curr = head
#         length = 0
#         while curr:
#             length += 1
#             curr = curr.next
#         for _ in range(length):
#             curr = head
#             p = curr
#             for _ in range(length):
#                 p = p.next
#                 if p == curr:
#                     return True
#         return False
