from linked_list.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 构造哑巴节点 dummy，最后返回 dummy.next, 以方便处理新链表的头节点。
        # 从头构建链表的时候，哑元节点是一个常用的技巧。
        curr = dummy = ListNode(0)
        carrier = 0

        while l1 or l2 or carrier:
            # l1没走到头、l2没走到头、还有进位三种情况

            # 求和，考虑可能有链表走到头
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carrier

            # 在尾部添加节点
            curr.next = ListNode(sum % 10)
            curr = curr.next

            # 更新进位，并向两个链表尾部前进
            carrier = sum // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
