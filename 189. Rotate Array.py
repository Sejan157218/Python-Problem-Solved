class Solution:
    def rotate(self, nums, k: int) -> None:
        lenNums=0
        lenNums2=len(nums)-1
        while lenNums<k:
            nums.insert(0,nums.pop())
            lenNums2-=1
            lenNums+=1
 


            
        return nums
s=Solution()
nums = [1,2,3,4,5,6,9]
k = 3
# nums=[-1]
# k=2
# nums =[1,2]
# k=3
# nums =[1,2]
# k=2
print(s.rotate(nums,k))