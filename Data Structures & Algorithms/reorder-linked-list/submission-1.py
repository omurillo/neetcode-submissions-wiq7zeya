# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        first_half = ListNode()
        first_half.next = head
        while fast and fast.next: 
            first_half = slow
            slow = slow.next
            fast = fast.next.next
        
        curr_node = slow.next
        prev_node = slow.next = None

        #reverse list
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        nodeA = head
        nodeB = prev_node
        while nodeB:
            tmp1, tmp2 = nodeA.next, nodeB.next
            nodeA.next = nodeB
            nodeB.next = tmp1
            nodeA, nodeB = tmp1, tmp2
