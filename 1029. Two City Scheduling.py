class Solution:
    def twoCitySchedCost(self, costs) -> int:
        minCost=0
        arr=[]
        for i in costs:
            minCost+=i[0]
            arr.append(i[1]-i[0])
        arr.sort()
        length=len(arr)//2
        for i in arr[:length]:
            minCost+=i
        return minCost




s=Solution()
costs = [[10,20],[30,200],[400,50],[30,20]]
costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
print(s.twoCitySchedCost(costs))