class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total=sum(nums)
        left=0
        for i,num in enumerate(nums):
            if left==(total-left-num):
                return i 
            left+=num
        return -1