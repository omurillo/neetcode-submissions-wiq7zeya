# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = l1
        node2 = l2
        total1 = 0
        total2 = 0
        index1 = 0
        index2 = 0
        while node != None or node2 != None:
            if node != None:
                total1 += node.val * (10 ** index1)
                node = node.next
                index1 += 1
            if node2 != None:
                total2 += node2.val * (10 ** index2)
                node2 = node2.next
                index2 += 1
        res = ListNode()
        head = res
        total = total1 + total2
        while total > 0:
            res.val = total % 10
            total = total // 10
            if total > 0:
                res.next = ListNode()
                res = res.next
        return head