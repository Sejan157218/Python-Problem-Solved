# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count=0
        temp=list1
        start=None
        end=None
        while temp:
            if count==a-1:
                start=temp
            if count==b:
                temp=temp.next
                end=temp
                break 

            count+=1
            temp=temp.next
        start.next=list2 
        
        while start.next:
            start=start.next
        start.next=end
        return list1
