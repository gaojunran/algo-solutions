"""
Solution1: HashSet.
遍历链表A，将各个节点存入一个集合中；
再遍历B，如果各节点有在集合中的就返回该节点。
"""
from typing import Optional

from linked_list.ListNode import ListNode


class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a_nodes = set()
        node = headA
        while node:
            a_nodes.add(node)
            node = node.next

        node = headB
        while node:
            if node in a_nodes:
                return node
            node = node.next

        return None


"""
Solution2: Stack.
将两个链表分别压入栈中，然后同时遍历两个栈，直到找到不同的节点。
"""
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s1, s2 = [], []
        p, q = headA, headB
        while p:
            s1.append(p)
            p = p.next
        while q:
            s2.append(q)
            q = q.next
        ans = None
        i, j = len(s1) - 1, len(s2) - 1
        while i >= 0 and j >= 0 and s1[i] == s2[j]:
            ans = s1[i]
            i, j = i - 1, j - 1
        return ans

"""
Solution3: Double Pointers.
先遍历一遍两个链表获得其长度，然后定义两个指针从前往后遍历两个链表。
"""
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        s1, s2 = 0, 0
        p, q = headA, headB
        # 计算长度
        while p:
            p = p.next
            s1 += 1
        while q:
            q = q.next
            s2 += 1
        # 长链表先走，需要讨论A和B谁更长两种情况
        p, q = headA, headB
        if s1 > s2:
            for i in range(s1 - s2):
                p = p.next
        else:
            for i in range(s2 - s1):
                q = q.next
        while p and q and p != q:
            p = p.next
            q = q.next
        return p
