from unittest import result


class Solution:
    def intersect(self, nums1, nums2) :
        result=[]
        for i in nums1:
            if i in nums2:
                if(result.count(i)<nums2.count(i)):
                    result.append(i)
        return result     
  

s=Solution()
nums1 = [1,2,2,1]
nums2 = [22,22]
nums1 = [4,9,5,4,4,4]
nums2 = [9,4,9,8,4,4,4,4]
print(s.intersect(nums1,nums2))