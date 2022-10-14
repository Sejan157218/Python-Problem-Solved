
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
             return (haystack.index(needle))
        else:
            return -1
        pass




# haystack = "sadbutsad"
# needle = "sad"
haystack = "leetcode"
needle = "leeto"
s=Solution()
print(s.strStr(haystack,needle))