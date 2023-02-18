import math

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        factors = [5, 3, 2]
        for factor in factors:
            while n % factor == 0:
                print(n,factor)
                n //= factor
                print(n,factor)
        return n == 1





s=Solution()
nums = 2
nums=19
# nums=6
nums=44444444
# nums=2147483647
# nums=5000000
# nums=10
print(s.isUgly(nums))