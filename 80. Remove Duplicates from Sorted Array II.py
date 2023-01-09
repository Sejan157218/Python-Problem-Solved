class Solution:
    def removeDuplicates(self, nums) -> int:

        deleteIndex=[]
        lengthOfNums=len(nums)
        pre=nums[0]
        count=1
        i=1
        
        while i<lengthOfNums:
            if pre==nums[i] and count<2:
                count+=1
                
            elif pre==nums[i] and count>=2:
                deleteIndex.append(i)
                count+=1
            else:
                pre=nums[i]
                count=1
            i+=1 

        lengthOfDeleteIndex=lengthOfNums-len(deleteIndex)
        count2=0
        for i in deleteIndex:
            nums.pop(i-count2)
            count2+=1
        return lengthOfDeleteIndex
        pass






s=Solution()
arr = [0,1,1,1,2,2,3,4,5,6,7,8]
nums = [0,0,1,1,1,1,2,3,3]
# nums = [1,1,1,1,2,2,3]
# nums = [1]
# arr=[1024,512,256,128,64,32,16,8,4,2,1]
print(s.removeDuplicates(nums))