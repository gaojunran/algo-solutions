from typing import Optional

from linked_list.ListNode import ListNode


class Solution:
    """
    两个一组。
    0 -> 1 -> 2 -> 3 -> 4 -> None
    这里对于while循环，可以有以下推导：
    node0 = dummy = ListNode(0, head)
    node1 = head
    --- iteration start ---
    node2 = node1.next
    node3 = node2.next
    # swap...
    node0 = node1
    node1 = node3
    --- iteration end --- use node 0 & 1 to predicate
    node2 = node1.next
    node3 = node2.next
    # swap...
    ...
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node0 = dummy = ListNode(0, head)
        node1 = head

        while node1 and node1.next:  # 至少有两个节点
            node2 = node1.next
            node3 = node2.next
            node0.next = node2  # 0 -> 2
            node2.next = node1  # 2 -> 1
            node1.next = node3  # 1 -> 3
            # 交换完，接着更新 node0, node1
            node0 = node1
            node1 = node3

        return dummy.next  # 返回新链表的头节点