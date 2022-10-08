from unittest import result


class Solution:
    def isValid(self, s: str) -> bool:
        
        arry=[]
        obt={
            "(":")",
            "{":"}",
            "[":"]"
        }

        for i in s:
            if i in obt:
                arry.append(i)
            elif len(arry)==0 or obt[arry.pop()] !=i:
                return False
        return len(arry)==0






# s = "(){"
s = "()[]{}"
# s = "(]"
# s="{[(]}"
sa=Solution()
print(sa.isValid(s))