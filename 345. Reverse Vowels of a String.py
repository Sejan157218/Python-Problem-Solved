class Solution:
    def reverseVowels(self, s: str) -> str:
        listOfs=list(s)
        vowel=['a', 'e', 'i', 'o','u','A', 'E', 'I', 'O','U']
        obj={}
        for i in range(0,len(listOfs)):
            if s[i] in vowel:
                obj[i]=s[i]
        lifOfObj=list(obj.keys())[::-1]
        i=0
        for j in range(0,len(listOfs)):
            if listOfs[j] in vowel:
                listOfs[j]=obj[lifOfObj[i]]
                i+=1
        result="".join(listOfs)
        return result
ss=Solution()
s = "hello"
s = "leetscode"
s="aA"
print(ss.reverseVowels(s))