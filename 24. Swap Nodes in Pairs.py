# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dammy=ListNode()
        curr=dammy
        count=1
        pre=None
        while head:
            if count%2==0:
                curr.next=ListNode(head.val)
                curr=curr.next
                curr.next=ListNode(pre)
                curr=curr.next
                pre=None
               
            else:
                pre=head.val
               
            count+=1
            head=head.next
        if pre!=None:
            curr.next=ListNode(pre)
            curr=curr.next
        return dammy.next


# Input: head = [1,2,3,4]
# Output: [2,1,4,3]