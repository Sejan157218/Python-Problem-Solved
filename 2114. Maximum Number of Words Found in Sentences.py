class Solution:
    def mostWordsFound(self, sentences):
        result=0
        for i in sentences:
            length=len((i.split(" ")))
            if length>result:
                result=length
        return result
        pass



s=Solution()

sentences = ["please wait", "continue to fight", "continue to win"]
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(s.mostWordsFound(sentences))