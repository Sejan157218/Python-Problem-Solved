class Solution:
    def myAtoi(self, s: str) -> int:
        strint=''
        intStr='0123456789'
        abc='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.'
        for i in s:
            if i in intStr:
                strint+=i
            elif i==" " and len(strint)!=0:
                break
            elif i=="-" and len(strint)==0:
                strint+=i
            elif i=="+" and len(strint)==0:
                strint+=i
            elif i in abc:
                break
            elif i=='-' or i=='+':
                break
        


        if strint:
            if strint[0]=='-' or strint[0]=='+':
                if len(strint)==1: 
                    return 0
            if strint[0]=='-' and len(strint)>1:
                result = int(strint)
                if result<-2147483648:
                    result=-2147483648
                return result
            elif strint[0]!='-':
                result=int(strint)
                if result>2147483647:
                    result = 2147483647
                return result
        return 0

ss=Solution()
s = "42"
s = "  4-.200---"
# s = "4193 with words"
# s="words and 987"
s="-91283472332"
# s="+-12"
s="-+12"
s="3.14159"
s="+1"
# s="+-12"
s="   +0 123"
print(ss.myAtoi(s))