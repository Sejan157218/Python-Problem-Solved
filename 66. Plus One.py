class Solution:
    def plusOne(self, digits):
        result=[]
        strEle=''
        for i in digits:
            strEle+=(str(i))
        newEle=int(strEle)+1
        for i in str(newEle):
            result.append(int(i))
        return result



digits = [9]
digits = [99]
# digits=[4,3,2,1]
s=Solution()
print(s.plusOne(digits))