from unittest import result


class Solution:
    def letterCombinations(self, digits: str):
        arr=[]
        obj={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if len(digits)==1:
            for i in obj[digits[0]]:
                arr.append(i)
        elif len(digits)==2:
           for i in range(0,len(digits)-1):
                for j in obj[digits[i]]:
                    for k in obj[digits[i+1]]:
                        arr.append(j+k)
        elif len(digits)==3:
           for i in range(0,len(digits)-2):
                for j in obj[digits[i]]:
                    for k in obj[digits[i+1]]:
                        for l in obj[digits[i+2]]:
                            arr.append(j+k+l)
        elif len(digits)==4:
           for i in range(0,len(digits)-3):
                for j in obj[digits[i]]:
                    for k in obj[digits[i+1]]:
                        for l in obj[digits[i+2]]:
                            for m in obj[digits[i+3]]:
                                arr.append(j+k+l+m)
        
        return arr






digits = "2"
s=Solution()
print(s.letterCombinations(digits))