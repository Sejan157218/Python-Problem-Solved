class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False




s=Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 300
print(s.searchMatrix(matrix,target))