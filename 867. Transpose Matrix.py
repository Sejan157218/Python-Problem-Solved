class Solution:
    def transpose(self, matrix):
        result=[]
        for i in range(len(matrix[0])):
            arr=[]
            for j in matrix:
                arr.append(j[i])
            result.append(arr)
        return result
        pass

s=Solution()
matrix = [[1,2,3]]
print(s.transpose(matrix))