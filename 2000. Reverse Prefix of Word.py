class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index=word.find(ch)
        return word[:index+1][::-1]+word[index+1:]


s=Solution()
word = "abcdefd"
ch = "d"
word = "xyxzxe"
ch = "z"
# word = "abcd"
# ch = "z"
print(s.reversePrefix(word,ch))