# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:       
        dammy=ListNode()
        curr=dammy
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        for i in arr:
           if arr.count(i)<2:
               curr.next=ListNode(i)
               curr=curr.next
        return dammy.next