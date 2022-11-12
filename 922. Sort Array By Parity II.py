class Solution:
    def sortArrayByParityII(self, nums):
        result=[]
        odd=[]
        even=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
               odd.append(nums[i])
            else:
                even.append(nums[i]) 
        i=0
        while i<len(odd):
            result.append(odd[i])
            result.append(even[i])
            i+=1
        return result
        




s=Solution()
# nums = [4,2,5,7]
nums = [2,3]
print(s.sortArrayByParityII(nums))