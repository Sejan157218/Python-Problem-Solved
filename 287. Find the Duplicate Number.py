class Solution:
    def findDuplicate(self, nums) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]
      

       
s=Solution()

nums = [0,0,1,1,1,1,2,3,3,5]

nums = [1,3,3,2,2]
print(s.findDuplicate(nums))