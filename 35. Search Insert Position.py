from unittest import result


class Solution:
    def searchInsert(self, nums, target: int) -> int:
        arr=[]
        if nums[0]>0 and target==0:
            return 0

        for i in range(0,len(nums)):
            if nums[i]==target:
                return i
            if nums[i]< target:
                arr.append(i)

        result=len(arr)-1 + 1
        return result 






# nums = [1]
# target = 2
# nums=[3,6,7,8,10]
# target = 5
# nums=[-1,3,5,6]
nums=[1,3,5,6]
target = 0
s=Solution()
print(s.searchInsert(nums,target))