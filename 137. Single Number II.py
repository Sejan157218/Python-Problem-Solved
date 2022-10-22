from unittest import result


class Solution:
    def singleNumber(self, nums) -> int:
        result=None   
        for i in range(len(nums)):
            rest=nums[:i] + nums[i+1:]
            if nums[i] not in rest:
                result=nums[i]

        return result
        pass

s=Solution()
n=[2,2,3,2]
n=[0,1,0,1,0,1,99]



print(s.singleNumber(n))