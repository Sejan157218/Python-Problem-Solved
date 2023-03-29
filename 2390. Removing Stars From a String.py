class Solution:
    def removeStars(self, s: str) -> str:
        arr=[]
        for i in s:
            if i =="*":
               arr.pop() 
            else:
                arr.append(i)
        
        # i=0
        # while i<len(arr):
        #     if arr[i]=="*":
        #         arr.pop(i)
        #         arr.pop(i-1)
        #         i-=1
                
        #     else:
        #         i+=1
        
         
        return "".join(arr)




ss=Solution()
s = "hello"
s = "leetscode"
s="leet**cod*e"
# s = "erase*****"

print(ss.removeStars(s))