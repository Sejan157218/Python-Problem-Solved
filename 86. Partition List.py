# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dammy=ListNode()
        curr=dammy
        head2=head
        while head2:
            if head2.val<x:
                curr.next=ListNode(head2.val)
                curr=curr.next
            head2=head2.next
        while head:
            if head.val>=x:
                curr.next=ListNode(head.val)
                curr=curr.next
            head=head.next
        return dammy.next