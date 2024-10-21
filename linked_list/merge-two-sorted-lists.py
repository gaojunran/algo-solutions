from typing import Optional

from linked_list.ListNode import ListNode

"""
Solution: Double Pointers.
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 使用一个哑结点来简化代码对头部的特殊处理
        cur = dum = ListNode(0)
        while list1 and list2:
            # 始终连接较小的节点，并更新指针
            if list1.val < list2.val:
                cur.next, list1 = list1, list1.next
            else:
                cur.next, list2 = list2, list2.next
            # 更新cur指针
            cur = cur.next
        # 连接剩余的节点
        cur.next = list1 if list1 else list2
        return dum.next

