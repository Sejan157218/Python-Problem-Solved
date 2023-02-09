# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
 
        nexthead=head
        while nexthead and nexthead.next:
            head=head.next
            nexthead=nexthead.next.next
            if head==nexthead:
                return True
        return False