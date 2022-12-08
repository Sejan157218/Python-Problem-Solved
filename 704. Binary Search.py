class Solution:
    def search(self, nums, target: int) -> int:
        left=0
        right=len(nums)-1
        mid=0
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1


s=Solution()
nums = [-1,0,3,5,9,12]
target = 9
nums = [-1,0,3,5,9,12]
target = 2

print(s.search(nums,target))