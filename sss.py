class Solution:
    def sortColors(self, nums) -> None:
        for i in range(1,len(nums)):
            element=nums[i]
            j=i-1

            while j>=0 and element<nums[j]:
                nums[j+1]=nums[j]
                print(nums[j],element)
                j-=1
            nums[j+1]=element
        print(nums)
        pass





s=Solution()

nums = [2,0,2,1,1,0]
print(s.sortColors(nums))