# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1str=''
        l2str=''
        while l1 or l2:
            if l1:
                l1str+=str(l1.val)    
                l1=l1.next
            if l2:
                l2str+=str(l2.val)
                l2=l2.next
        dammy=ListNode()
        curr=dammy
        for i in str(int(l1str[::-1])+int(l2str[::-1]))[::-1]:
            curr.next=ListNode(int(i))
            curr=curr.next
        return dammy.next