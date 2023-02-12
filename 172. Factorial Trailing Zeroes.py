class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact = 1
        for i in range(1, n+1):
            fact = fact * i

        factStr=str(fact)
        lengthOffactStr=len(factStr)-1
        result=0
        
        while lengthOffactStr>0:
            if factStr[lengthOffactStr]=="0":
                result+=1
            else:
                break
            lengthOffactStr-=1
        return result

solution=Solution()
n=10000
print(Solution().trailingZeroes(n))

