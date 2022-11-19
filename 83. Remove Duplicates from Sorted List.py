# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dammy=ListNode()
        curr=dammy
        pre=None
        while head:
            if pre!=head.val:
                curr.next=ListNode(head.val)
                pre=head.val
                curr=curr.next
            head=head.next
        return dammy.next