class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        while left<=right:
            DividingNumbers=True
            for i in str(left):
                num=int(i)
                if num!=0 and left % num !=0 or '0' in str(left):
                   DividingNumbers=False
                   break
            if DividingNumbers:
                result.append(left) 
            left+=1
        return result




s=Solution()
left = 1
right = 50000
# arr=[1024,512,256,128,64,32,16,8,4,2,1]
print(s.selfDividingNumbers(left,right))