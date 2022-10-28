class Solution:
    def reverseString(self, s):
        i=0
        k=len(s)-1
        j=len(s)/2
        while k>=j:
            temp2=s[k]
            temp1=s[i]
            s[i]=temp2
            s[k]=temp1
            k-=1
            i+=1
            
        print(s)


s=Solution()
ss = ["h","e","l","l","o","3"]
print(s.reverseString(ss))