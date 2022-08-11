
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        array=[]
        count=0;
        for i in range(len(nums)):
            if nums[i]==1:
               count +=1; 
            elif nums[i]==0:
                array.append(count)
                count =0;
        if len(array):
            if max(array) > count:
                return max(array);
        
        return count;



nums = [1]
solution=Solution()

print(Solution().findMaxConsecutiveOnes(nums))