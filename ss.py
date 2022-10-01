# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head=None;
    def insert_arr(self,val):
        if self.head is None:
            self.head=ListNode(val,self.head)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=ListNode(val)

    def print(self):
        itr=self.head
        listr=[]
        while itr:
            listr.append(itr.val)
            itr=itr.next
        print(listr)
    def mergeTwoLists(self, list1,list2):

        list=sorted(list1+list2)

        for i in list:
            self.insert_arr(i)
        

sl=Solution()
sl.mergeTwoLists([1,2,4],[1,3,4])
sl.print()