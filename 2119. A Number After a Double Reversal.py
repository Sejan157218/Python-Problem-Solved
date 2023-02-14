class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        numReverse=int(str(num)[::-1])
        doubleReverse=int(str(numReverse)[::-1])
        if doubleReverse==num:
            return True
        return False
       


s=Solution()
num = 1800
num = 526
print(s.isSameAfterReversals(num))