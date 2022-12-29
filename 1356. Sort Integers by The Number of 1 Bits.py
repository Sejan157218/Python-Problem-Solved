class Solution:
    def sortByBits(self, arr):
        arr.sort()
        for i in range(1,len(arr)):
            element=arr[i]
            bitCount=bin(element)[2:].count('1')

            j=i-1
            while j>=0 and bin(arr[j])[2:].count('1')>bitCount:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=element

        return arr
            # print(i,"->",bitCount)
            
        
        pass



s=Solution()
arr = [0,1,2,3,4,5,6,7,8]
# arr=[1024,512,256,128,64,32,16,8,4,2,1]
print(s.sortByBits(arr))