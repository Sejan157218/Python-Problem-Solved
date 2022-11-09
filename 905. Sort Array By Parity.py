class Solution:
    def sortArrayByParity(self, nums):
        nums.sort()
        arrOdd=[]
        arrEven=[]
        for i in nums:
           if i%2==0:
            arrOdd.append(i)
           else:
            arrEven.append(i)
        return arrOdd+arrEven



s=Solution()
head = [1,4,3,2,5]
print(s.sortArrayByParity(head))