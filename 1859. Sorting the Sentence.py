class Solution:
    def sortSentence(self, s: str) -> str:
        obj={}
        number=['1','2','3','4','5','6','7','8','9'," "]
        string=""
        arr=[]
        for i in s:
            if i not in number:
                string+=i
            else:
                if i!=" ":
                    arr.append(int(i))
                    obj[i]=string
                    string=""
        
        for i in range(1,len(arr)):
            elemnet=arr[i]
            j=i-1

            while j>=0 and elemnet<arr[j]:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=elemnet
        
        result=""
        for i in arr:
            result+=obj[str(i)]+" "
        

        return result[:-1]
         





ss=Solution()

s = "Myself2 Me1 I4 and3"
print(ss.sortSentence(s))