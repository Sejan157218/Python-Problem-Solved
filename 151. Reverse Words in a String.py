class Solution:
    def reverseWords(self, s: str) -> str:
        arr=s.split(" ")
        deleteSpace=[i for i in arr if i!='']
        return ' '.join(deleteSpace[::-1])
   



ss=Solution()
s = "  hello world  "
print(ss.reverseWords(s))