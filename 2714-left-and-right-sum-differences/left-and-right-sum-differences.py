class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        lst=[]
        for i in range(len(nums)):
            ls=prefix[i]-nums[i]
            total=prefix[len(nums)-1]
            rs=total-prefix[i]
            lst.append(abs(ls-rs))
        return lst