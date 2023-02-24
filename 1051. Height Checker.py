class Solution:
    def heightChecker(self, heights) -> int:
        sortHeight=[i for i in heights]
        heights.sort()
        count=0
        for i in range(len(heights)):
            if sortHeight[i]!=heights[i]:
                count+=1
        return count

s=Solution()
heights = [1,1,4,2,1,3]
print(s.heightChecker(heights))