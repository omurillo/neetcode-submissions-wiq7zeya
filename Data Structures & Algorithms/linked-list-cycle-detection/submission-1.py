# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next
        while slow:
            if slow == fast:
                return True
            slow = slow.next
            if fast and fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False
        return False