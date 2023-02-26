class Solution:
    def smallerNumbersThanCurrent(self, nums):
        arr=[i for i in nums]
        arr.sort()
        result=[]
        for i in nums:
            result.append(arr.index(i))
        return result


s=Solution()
nums = [8,1,2,2,3]

print(s.smallerNumbersThanCurrent(nums))