class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            rest=s[:i]+s[i+1:]
            if s[i] not in rest:
                return i
        return -1



s=Solution()
ss = "leetcode"
ss= "aabb"
ss = "loveleetcode"
print(s.firstUniqChar(ss))