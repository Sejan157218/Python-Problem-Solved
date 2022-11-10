class Solution:
    def findDifference(self, nums1, nums2):
        # i=0
        # j=0
        # distinctNums1=[]
        # distinctNums2=[]
        # while i<len(nums1) or j<len(nums2):
        #     if  i<len(nums1) and nums1[i] not in nums2 and nums1[i] not in distinctNums1:
        #         distinctNums1.append(nums1[i])  
        #     if j<len(nums2) and nums2[j] not in nums1 and nums2[j] not in distinctNums2:
        #         distinctNums2.append(nums2[j]) 
        #     i+=1
        #     j+=1
        # return ([distinctNums1,distinctNums2])
        s1=set(nums1)
        s2=set(nums2)
        result=[list(s1-s2),[list(s2-s1)]]
        return result


# [[-80,-15,-81,-28,-61,63,14,-45,-35,-10],[-1,-40,-44,41,10,-43,69,10,2]]
# [[-81,-35,-10,-28,-61,-45,-15,14,-80,63],[-1,2,69,-40,41,10,-43,-44]]
[[-61, -28, 14, -81, -80, -15, -45, -10, -35, 63], [[2, 69, 41, 10, -44, -43, -40, -1]]]






s=Solution()
nums1 = [1,5]
nums2 = [2,4,6]
nums1=[-80,-15,-81,-28,-61,63,14,-45,-35,-10]
nums2=[-1,-40,-44,41,10,-43,69,10,2]
print(s.findDifference(nums1,nums2))