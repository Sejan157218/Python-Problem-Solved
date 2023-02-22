class Solution:
    def duplicateZeros(self, arr) -> None:
        i=0
        lengthOfArr=len(arr)
        while i<lengthOfArr:
            if arr[i]==0:
                arr.insert(i+1,0)
                arr.pop()
                i+=2
            else:
                i+=1
        return arr


s=Solution()
arr = [1,0,2,3,0,4,5,0]
print(s.duplicateZeros(arr))