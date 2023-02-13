class Solution:
    def prefixCount(self, words, pref: str) -> int:
        lengthOfpref=len(pref)
        count = 0
        
        for i in words:
            print(i[0:lengthOfpref])
            if i[0:lengthOfpref] == pref:
                count +=1
        return count


ss=Solution()
words = ["pay","attention","practice","attend"]
pref = "att"
print(ss.prefixCount(words,pref))