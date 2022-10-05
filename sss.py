class Solution:
    def removeElement(self, nums, val: int) -> int:
        i=0
        # for i in range(0,len(nums)-1):

        while i<len(nums):
            if nums[i]==val:
            #     # print(i,nums[i])
            #     # temp=nums[i]
            #     # nums[i]=nums[i+1]
            #     # nums[i+1]=temp
                del nums[i]
                i=i-1
            i+=1

        print(nums)
        return (len(nums))        

        pass



nums = [0,1,2,2,3,0,4,2]
val = 2
s=Solution()
print(s.removeElement(nums,val))

