from linked_list.ListNode import ListNode

"""
Solution: Double Pointers.
"""
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            # 链表长度为奇数时，fast走到尾节点
            # 链表长度为偶数时，fast走到尾节点后面的null
            # 特别地，如果要求返回第一个中间节点，fast走到尾节点的前驱，
            # 此时修改while条件为while fast.next and fast.next.next
            fast = fast.next.next
            slow = slow.next
        return slow