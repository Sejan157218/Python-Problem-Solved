class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return None
        curr,temp=head, head.next.next
        while temp and temp.next:

            curr=curr.next
            temp=temp.next.next
        curr.next=curr.next.next    
        return head



# 14%
# class Solution:
#     def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dammy=addNode=ListNode()
#         temp=curr=head
        
#         while temp and temp.next:
#             addNode.next=ListNode(curr.val)
#             addNode=addNode.next
#             curr=curr.next
#             temp=temp.next.next
#         addNode.next=curr.next
#         return dammy.next