class Solution:
    def merge(self, nums1, m, nums2, n: int) -> None:

        for i in range(m,len(nums1)):
            nums1.pop()
 
        for i in range(0,n):
            nums1.append(nums2[i])
             
        nums1.sort()
        return nums1



# nums1 = [0]
# m = 0
# nums2 = [1]
# n = 1

# nums1 = [1]
# m = 1
# nums2 = []
# n = 0

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# nums1 = [4,5,6,0,0,0]
# m = 3
# nums2 = [1,2,3]
# n = 3
s=Solution()

print(s.merge(nums1,m,nums2,n))
 