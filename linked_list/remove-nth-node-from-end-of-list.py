from linked_list.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 第一次遍历，计数链表长度
        curr = head
        size = 0
        while curr:
            curr = curr.next
            size += 1

        # 第二次遍历至第 N - n, 即倒数第 n+1 个节点处
        # 这一行将原链表改造成带哨兵的链表，排除删除时的特殊情况
        curr = dummy = ListNode(0, head)
        for _ in range(size - n):
            curr = curr.next

        # 删除子节点，即倒数第 n 个节点
        curr.next = curr.next.next

        return dummy.next


class Solution2:
    """
    双指针法。设n = 2, N = 5
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
                            ^
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
                  ^r
    dummy -> 1 -> 2 -> 3 -> 4 -> 5
                       ^l        ^r
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 和上面的解类似，引入哨兵节点
        l = r = dummy = ListNode(0, head)

        # 右指针先前进 n 次
        for _ in range(n):
            r = r.next

        # 左右指针同步前进，直至右指针抵达边界
        while r.next:
            r = r.next
            l = l.next
        # 现在得到的 l.next 是倒数第n个节点
        l.next = l.next.next
        return dummy.next
