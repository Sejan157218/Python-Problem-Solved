


class Solution:
    def generate(self, numRows: int):
        result=[[1]]
        if numRows==1:
            return result
        i=0
        while i<numRows-1:
            if i<(len(result)):
                result.append(self.SumOfArray(result[i]))
            i+=1
        return result
    def SumOfArray(self,arr):   
        res=[]
        for j in range(len(arr)-1):
            res.append(arr[j]+arr[j+1])
        return  [1]+res+[1]

  

s=Solution()
numRows = 5

print(s.generate(numRows))