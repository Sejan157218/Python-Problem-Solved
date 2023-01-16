class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        length=len(arr)
        print(length)
        i=len(arr)//2
        j=0
        maxNum=-1
        maxIndex=0
        while i<length:
            if arr[j]>maxNum:
                maxNum=arr[j]
                maxIndex=j
            if arr[i]>maxNum:
                maxNum=arr[i]
                maxIndex=i
            i+=1
            j+=1
        return maxIndex
        print(maxNum,maxIndex)
s=Solution()
arr = [0,1,1,1,2,2,3,4,5,6,7,8]
nums = [0,0,1,1,1,1,2,3,3,5]

arr=[1024,512,256,128,64,32,16,8,4,2,1,12]
print(s.peakIndexInMountainArray(arr))