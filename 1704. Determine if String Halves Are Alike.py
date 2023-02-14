class Solution:
    def halvesAreAlike(self, s):
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        length=len(s)//2
        arr1=s[:length]
        arr2=s[length:]
        i=0
        count=0
        count2=0
        while i<len(arr1):
            if arr1[i] in vowels:
                count+=1
            if arr2[i] in vowels:
                count2+=1
            i+=1
        if count==count2:
            return True

        return False
        




ss=Solution()
s = "textbook"
s = "book"
print(ss.halvesAreAlike(s))