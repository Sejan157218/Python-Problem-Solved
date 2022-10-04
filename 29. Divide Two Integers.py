class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend/divisor)
        if result >2147483647:
            return 2147483647;
        return result


sl=Solution()

print(sl.divide(-2147483648,-1))
print(sl.divide(1,-1))
print(sl.divide(-1,-1))