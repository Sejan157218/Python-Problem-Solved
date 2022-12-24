# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dammy=ListNode()
        curr=dammy
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        arr.sort()
        for i in arr:
            curr.next=ListNode(i)
            curr=curr.next
        return dammy.next




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Limit Exceeded
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dammy=ListNode()
        curr=dammy
        while head:
            head2=head
            while head2:
                if head.val>head2.val:
                    temp=head.val
                    head.val=head2.val
                    head2.val=temp
                head2=head2.next
            curr.next=ListNode(head.val)
            curr=curr.next
            head=head.next
        return dammy.next