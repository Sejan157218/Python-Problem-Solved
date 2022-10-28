from unittest import result


class Solution:
    def hammingWeight(self, n: int) -> int:
        result=0
        for i in str(n):
            if int(i)==1:
                result+=1

        return result



s=Solution()
n = "00000000000000000000000000001011"
n = 11111111111111111111111111111101
print(s.hammingWeight(n))