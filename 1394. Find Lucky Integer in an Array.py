class Solution:
    def findLucky(self, arr):
        setOfArr=list(set(arr))
        result=-1
        for i in setOfArr:
            if arr.count(i)==i and result<i:
                result=i

        return result




s=Solution()
arr = [2,2,3,4]
print(s.findLucky(arr))