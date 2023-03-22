class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        for i in range(len(edges)):
            for j in edges[i]:
                if j in edges[i+1]:
                    return j
                


# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2