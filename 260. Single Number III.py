class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        nums.sort()
        length=len(nums)
        i=0
        arr=[]

        while i<length-1:
            if nums[i]!=nums[i+1]:
                arr.append(nums[i])
                i+=1
            else:
                i+=2
        if nums[length-1]!=nums[length-2]:
            arr.append(nums[length-1])
        return arr

# nums = [1,2,1,3,2,5]
# Output: [3,5]