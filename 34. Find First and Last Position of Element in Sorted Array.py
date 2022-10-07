class Solution:
    def searchRange(self, nums, target: int) :
        result=[]
        for i in range(0,len(nums)):
            if nums[i]==target:
                if len(result)<2:
                    result.append(i)
                elif len(result)==2:
                    result[1]=i
        if len(result)==1:
            result.append(result[0])
        if len(result)==0:
            result=[-1,-1]
        
        
        return result


nums = [5,7,7,8,8,10]
target = 8

# nums = [5,7,7,8,8,10]
# target = 6

# nums = []
# target = 0

# nums = [1]
# target = 1

# nums = [3,3,3]
# target = 3

s=Solution()

print(s.searchRange(nums,target))