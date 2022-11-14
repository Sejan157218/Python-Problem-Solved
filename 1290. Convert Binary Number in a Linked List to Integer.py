# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num=''
        while head:
            num+=str(head.val)
            head=head.next
        return int(num, 2)
s=Solution()
Input: head = [1,0,1]
Output: 5
