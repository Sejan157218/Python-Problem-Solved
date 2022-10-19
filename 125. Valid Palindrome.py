class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(s)
        arr="abcdefghijklmnopqrstuvwxyz0123456789"
        str=''
        for i in s:
            if i.lower() in arr:
               str +=i.lower()
        print(str,str[::-1])
        if str==str[::-1]:

            return True
        else:
            return False






ss = "A man, a plan, a canal: Panama"
ss =" "
ss = "race a car"
ss ="OP"
ss ="aoa"
ss ="1a2"
# ss =



s=Solution()
print(s.isPalindrome(ss))

