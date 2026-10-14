class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        sum=0
        original=x
        while x>0:
            sum= sum*10 + x%10
            x=x//10
        return sum==original  