from linked_list.middle_of_the_linked_list import Solution as MiddleOfTheLinkedList
from linked_list.reverse_linked_list import Solution as ReverseLinkedList

"""
Solution1: Linked List reversal + Double Pointers
找到链表的中间节点，反转后半部分链表，然后比较前后两部分链表是否相同。
"""
from typing import Optional

from linked_list.ListNode import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        middle = MiddleOfTheLinkedList.middleNode(head)
        # 注意，根据原题这会返回第二个中间节点
        head2 = ReverseLinkedList.reverseList(middle)
        # 反转后链表如图所示：
        # 1 -> 2 -> 3 -> 4 <- 3 <- 2 <- 1 （奇数）
        #                ^ 中间节点指向None
        # 1 -> 2 -> 3 -> 4 <- 4 <- 3 <- 2 <- 1 （偶数）
        #                     ^ 中间节点指向None
        while head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        return True
