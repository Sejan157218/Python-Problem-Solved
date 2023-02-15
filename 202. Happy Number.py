class Solution:
    def isHappy(self, n: int) -> bool:
        underTenNum=self.underTen(n)     
        if underTenNum==1 or underTenNum==7:
            return True
        if underTenNum>1 and underTenNum<10:
            return False

    def underTen(self,m):
        if m<10:
            return m
        count=0
        for i in str(m):
            squre=int(i)**2
            count +=squre
        return self.underTen(count)






s=Solution()
nums = 2
nums=19
nums=2147483647
nums=7
print(s.isHappy(nums))