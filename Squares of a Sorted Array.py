class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        result=[]
        for i in nums:
            result.append(i**2)
        result.sort()
        return result;




nums = [-4,-1,0,3,10]
solution=Solution()

print(Solution().sortedSquares(nums))