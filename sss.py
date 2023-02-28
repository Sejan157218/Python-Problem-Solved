class Solution:
    def findTheArrayConcVal(self, nums) -> int:
        # if len(nums)==0:
        #     return n
        # elif len(nums)==1:
        #     return n+nums[0]
        # else:
        #     n+=int(str(nums[0])+str(nums[-1]))
            
        #     return self.findTheArrayConcVal(nums[1:-1],n)
        result=0
        while len(nums)>=0:
            if len(nums)==0:
                return result
            elif len(nums)==1:
                return result+nums[0]
            else:
                result+=int(str(nums[0])+str(nums[-1]))
                nums=nums[1:-1]
        pass




s=Solution()
nums = [8,1,2,5,2,3]

print(s.findTheArrayConcVal(nums))