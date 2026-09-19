class Solution:
    def romanToInt(self, s: str) -> int:
        roman={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 
        'M': 1000}
        total=0
        for i in range(len(s)):
            num1=roman[s[i]]
            if i+1<len(s):
                num2=roman[s[i+1]]
                if num1>=num2:
                    total+=num1
                else:
                    total-=num1
            else:
                total+=num1
        return total
                