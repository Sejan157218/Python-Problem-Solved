class Solution:
    def reverse(self, x: int) -> int:
        result=None
        if x>0:
            s=str(x)
            stsr=''
            for i in s:
                stsr=i+stsr
            resultInt=int(stsr)
            if resultInt>2147483647:
                result=0
            else:
                result=resultInt
        else:
            s=str(x*-1)
            stsr=''
            for i in s:
                stsr=i+stsr
            resultInt=int(stsr)
            if resultInt>2147483647:
                result=0
            else:
                result=resultInt *-1

        return result

s=Solution()
print(s.reverse(2147483648))