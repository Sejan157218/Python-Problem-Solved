class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        result=[]
        for i in nums:
            if len(str(i)) %2==0:
                result.append(i)
        return len(result)







nums = [555,901,482,1771]
solution=Solution()

print(Solution().findNumbers(nums))