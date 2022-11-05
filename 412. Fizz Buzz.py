
class Solution:
    def fizzBuzz(self, n: int):
        result=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                result.append("FizzBuzz")
               
            elif i%3==0:
                result.append("Fizz")  
               
            elif i%5==0:
                result.append("Buzz")
               
            else:
                result.append(str(i)) 
        return result
s=Solution()
# n=5
# n=3
n = 15
print(s.fizzBuzz(n))



class Solution:
    def fizzBuzz(self, n: int):
        result=[]
        for i in range(1,n+1):
            res=''    
            if i%3==0:
                res+="Fizz"
            if i%5==0:
                res+="Buzz"
            result.append(res if res else str(i))
        return result
s=Solution()
# n=5
# n=3
n = 15
print(s.fizzBuzz(n))