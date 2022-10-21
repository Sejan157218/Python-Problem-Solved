from unittest import result


class Solution:
    def mySqrt(self, x: int) -> int:
        result=int(x ** .5)
        return result

s=Solution()
x = 8
x = 4
x=25
x=2000000
print(s.mySqrt(x))