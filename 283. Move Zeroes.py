class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countZero=nums.count(0)
        countNum=0
        i=0
        while i<len(nums):
            if nums[i]==0 :
                nums.append(nums.pop(i))
                countNum+=1
                i-=1
            if countZero==countNum:
                break
            i+=1

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]