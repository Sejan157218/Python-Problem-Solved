# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


class Solution:
    def romanToInt(self, s: str) -> int:
        I=1
        V =5
        X =10
        L = 50
        C =100
        D=500
        M=1000
        CM = 900
        XC = 90 
        IV = 4
        IX=9
        CD=400
        DC=600
        XL=50

        count=0
        # for i in range(0,len(s)-1):
        #     if s[i]+s[i+1]=="CM" or s[i]+s[i+1]=="XC" or s[i]+s[i+1]=="IV":
        #         print("pass")
        #         new=s[i]+s[i+1]
        #         count += eval(new)
        #         print(i,"len(s)-1-i")
        #         if len(s)-1-i<=2:
        #             i+=2
        #     else:
        #         count += eval(s[i])
        #         print(s[i])
        # return count
        i=0;
        if len(s)==1:
            return eval(s[0])
        while i<len(s)-1:
            # print(i,"i")
        
            print(s[i])
            if s[i]+s[i+1]=="CM" or s[i]+s[i+1]=="XC" or s[i]+s[i+1]=="IV" or s[i]+s[i+1]=="IX" or s[i]+s[i+1]=="CD" or s[i]+s[i+1]=="DC" or s[i]+s[i+1]=="XL":
               
                # print("i",i,len(s)-1)
                if (len(s)-2)-i==1:
                    # print("i,i,len(s)-1")
                    new=s[i]+s[i+1]
                    count += (eval(new) + eval(s[i+2]))
                    # print((eval(new) + eval(s[i+2])))
                    break
                else:
                    new=s[i]+s[i+1]
                    count += eval(new)
                    # print("pass")
                    i+=2
                # print(i,'print(i)')
            else:
                # print(i,"i")
                if i == len(s)-2:
                    # print(eval(s[i+1]),s[i])
                    count += (eval(s[i]) + eval(s[i+1]))
                    i+=1
                else:
                    count += eval(s[i])
                    i+=1
        return count

s=Solution()
print(s.romanToInt("D"))