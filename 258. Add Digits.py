class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num
        integer=0
        for i in str(num):
            integer+=int(i)
        return self.addDigits(integer)  

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.