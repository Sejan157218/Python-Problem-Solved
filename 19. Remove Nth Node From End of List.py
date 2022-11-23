# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head2=head
        count=0
        while head2:
            count+=1
            head2=head2.next
        dammy=ListNode()
        curr=dammy
        count2=0
        while head:
            if count2==count-n:
                curr.next=head.next
                break
            else:
                curr.next=ListNode(head.val)
                curr=curr.next
            count2+=1
            head=head.next
        return dammy.next