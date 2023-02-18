class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result=[]
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                result.append(nums[i])
        return result


nums = [4,3,2,7,8,2,3,1]