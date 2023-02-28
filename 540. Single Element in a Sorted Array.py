class Solution:
    def singleNonDuplicate(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        i=0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                return nums[i]
            else:
                i+=2
        return nums[-1]


s=Solution()
nums = [1,1,2,3,3,4,4,8,8]
nums = [1,1,2]
print(s.singleNonDuplicate(nums))