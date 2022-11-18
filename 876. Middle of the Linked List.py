# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dammy=ListNode(0)
        curr=dammy
        head2=head
        count =0
        while head2:
            count +=1
            head2=head2.next
        middle=count//2
        count2 =0
        while head:
            count2 +=1
            if count2>middle:
              return head
            else:
                head=head.next