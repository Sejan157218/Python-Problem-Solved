class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=(str(x))
        y=(str(x)[::-1])
        if x==y:
            return True
        else:
            return False

solution=Solution()

print(Solution().isPalindrome(-121))