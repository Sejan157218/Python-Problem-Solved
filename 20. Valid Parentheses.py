from unittest import result


class Solution:
    def isValid(self, s: str) -> bool:
        
        # stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        # for parenthese in s:
      
        #     if parenthese in pchar:
        #         stack.append(parenthese)
        #     elif pchar[stack.pop()] != parenthese:
        #         return False
   
        # return len(stack) == 0


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