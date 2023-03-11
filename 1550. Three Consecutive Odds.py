class Solution:
    def threeConsecutiveOdds(self, arr) -> bool:
        if len(arr)<3:
            return False
        i=0
        while i<len(arr)-2:
            if arr[i]%2!=0 and arr[i+1]%2!=0 and arr[i+2]%2!=0:
                return True
            i+=1
        return False

s=Solution()
arr = [1,2,34,3,4,5,7,23,12]
arr = [5,7,23]
print(s.threeConsecutiveOdds(arr))