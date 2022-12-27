class Solution:
    def sortEvenOdd(self, nums):
        result = []
        odd=[]
        even=[]
        for i,n in enumerate(nums):
            if i%2==1:
                odd.append(n)
            else:
                evenCount+=1
                even.append(n)

        for i in range(1,len(odd)):
            element=odd[i]
            j=i-1

            while j>=0 and element>odd[j]:
                odd[j+1]=odd[j]
                j-=1
            odd[j+1]=element

        for i in range(1,len(even)):
            element=even[i]
            j=i-1
            while j>=0 and element<even[j]:
                even[j+1]=even[j]
                j-=1
            even[j+1]=element

        for i,n in enumerate(nums):
            if i%2==1:
                result.append(odd.pop(0))
            else:
                result.append(even.pop(0))

        return result

        

s=Solution()

nums = [4,1,2,3]
nums =[36,45,32,31,15,41,9,46,36,6,15,16,33,26,27,31,44,34]
print(s.sortEvenOdd(nums))