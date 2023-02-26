class Solution:
    def checkIfExist(self, arr) -> bool:
        for i in range(len(arr)):
            if arr[i]*2 in arr:
                j=arr.index(arr[i]*2)
                if i!=j:
                    return True
            if arr[i]/2 in arr:
                j=arr.index(arr[i]/2)
                if i!=j:
                    return True
        return False

s=Solution()
arr = [10,2,5,3]
print(s.checkIfExist(arr))