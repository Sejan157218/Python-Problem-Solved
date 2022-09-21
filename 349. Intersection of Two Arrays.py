def intersection(nums1, nums2):
    result=[]
    for i in nums1:
        for j in nums2:
            if i==j and i not in result:
                result.append(i)
    return result;

nums1 = [1,2,2,1]
nums2 = [2,2]

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

result=intersection(nums1,nums2)
print(result)