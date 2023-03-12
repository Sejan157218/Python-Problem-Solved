class Solution:
    def findRestaurant(self, list1, list2) :
        result=[]
        mimSumIndex=1000000
        for i in range(len(list1)):
            if list1[i] in list2:
                sumOfIndex=i+list2.index(list1[i])
                if sumOfIndex<mimSumIndex:
                    mimSumIndex=sumOfIndex
                    result+=[list1[i]]
                elif sumOfIndex==mimSumIndex:
                    mimSumIndex=sumOfIndex
                    result+=[list1[i]]
        return result
    


s=Solution()
list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
print(s.findRestaurant(list1,list2))