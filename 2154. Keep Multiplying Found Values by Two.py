class Solution:
    def findFinalValue(self, nums, original) -> int:
        if original in nums:
            return self.findFinalValue(nums,original*2)
        else:
            return original




s=Solution()
nums = [5,3,6,1,12]
original = 3
print(s.findFinalValue(nums,original))