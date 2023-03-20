class Solution:
    def restoreString(self, s: str, indices) -> str:
        obj={}
        for i in range(len(indices)):
            obj[indices[i]]=s[i]
        indices.sort()
        result=''
        for i in indices:
            result+=obj[i]
        return result
        pass



s=Solution()
ss = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(s.restoreString(ss,indices))