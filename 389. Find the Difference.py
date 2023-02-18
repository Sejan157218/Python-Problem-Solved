class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        string='abcdefghijklmnopqrstuvwxyz'
        for i in string:
            if s.count(i) !=t.count(i):
                return i
            pass
        



ss=Solution()
s = "abcd"
t = "abcde"
print(ss.findTheDifference(s,t))