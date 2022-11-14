class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(list(set(s)))
        if len(t)!= len(s):
            return False
        letters = list(set(s))
        for i in letters:
            if s.count(i)!=t.count(i):
                return False
        return True


ss=Solution()
s = "anagraa"
t = "nagaram"
s = "rat"
t = "car"
print(ss.isAnagram(s,t))