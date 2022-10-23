class Solution:
    def getRow(self, rowIndex: int):
        result=[[1]]
    
        i=0
        while i<rowIndex:
            if i<(len(result)):
                result.append(self.SumOfArray(result[i]))
            i+=1
        return result[rowIndex]
    def SumOfArray(self,arr):   
        res=[]
        for j in range(len(arr)-1):
            res.append(arr[j]+arr[j+1])
        return  [1]+res+[1]

  

s=Solution()
numRows = 3

print(s.getRow(numRows))