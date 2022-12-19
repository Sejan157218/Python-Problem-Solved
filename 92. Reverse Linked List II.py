# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dammy=ListNode()
        curr=dammy


        reverse=None

        if left<=right:
            count=1
            while head:
                if count>=left and count<=right:
                    temp=ListNode(head.val)
                    temp.next=reverse
                    reverse=temp
                    if count==right:
                       while reverse:
                        curr.next=ListNode(reverse.val)
                        curr=curr.next
                        reverse=reverse.next
                else:
                    curr.next=ListNode(head.val)
                    curr=curr.next
                count+=1
                head=head.next
            return dammy.next
                
        else:
            curr.next=head

        return dammy.next
