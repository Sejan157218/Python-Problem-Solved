def removeDuplicates(nums):
    l=1
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            nums[l]=nums[i]
            # nums.remove(nums[i])
            l+=1
          
    print(nums)
    return l

   

nums = [0,0,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
