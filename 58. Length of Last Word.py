class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if len(str)==0:
            return 0
        strSplit=s.split(" ")
        arr=[]
        for i in strSplit:
            if len(i)>0:
                arr.append(i)

        return len(arr[-1])



# str = "   fly me   to   the moon  "
# str="Hello World"
str=""
s=Solution()
print(s.lengthOfLastWord(str))