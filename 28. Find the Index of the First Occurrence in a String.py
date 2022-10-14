
class Solution:
    # def strStr(self, haystack: str, needle: str) -> int:
        # if needle in haystack:
        #      return (haystack.index(needle))
        # else:
        #     return -1
    # def strStr(self, haystack, needle):
        # nl, ml = len(needle), len(haystack)
        # if nl == 0:
        #     return nl
        # if ml < nl:
        #     return -1
        # for i in range(ml - nl + 1):
        #     print(i,ml,nl)
        #     print(haystack[i:i+nl])
        #     if haystack[i:i+nl] == needle:
        #         return i
        # return -1
      def strStr(self, haystack, needle):
        return haystack.find(needle)
       




haystack = "sasdbutsad"
needle = "sad"
# haystack = "leetcode"
# needle = "leeto"
s=Solution()
print(s.strStr(haystack,needle))