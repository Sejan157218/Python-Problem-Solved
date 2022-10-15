class Solution:
    def longestCommonPrefix(self, strs):
        result=''
        str=''
        for i in strs[0]:
            str +=i
            if all(str in strss and str[0:len(str)]==strss[0:len(str)] for strss in strs):
                result=str
        return result  



s=Solution()
strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
# strs=["c","acc","ccc"]
# strs=["a"]
# strs=["ab", "a"]
# strs=["flower","flower","flower","flower"]
# strs=["abca","aba","aaab"]
print(s.longestCommonPrefix(strs))