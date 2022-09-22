from xml.sax.handler import property_interning_dict


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr=[ *nums1 , *nums2 ]
        for i in range(0,len(arr)):
            for j in range (i +1,len(arr)):
                if arr[i]>arr[j]:
                    temp=arr[j]
                    arr[j]=arr[i]
                    arr[i]=temp
        if len(arr) % 2==0:
            mid=int(len(arr)/2)
            result=(arr[mid] + arr[mid-1])/2
            return result;
        else:
            mid=(int(len(arr) / 2))
            result= float(arr[mid])
            return result
   







nums1 = [1,2]
nums2 = [3,4]

solution=Solution()

print(Solution().findMedianSortedArrays(nums1,nums2))