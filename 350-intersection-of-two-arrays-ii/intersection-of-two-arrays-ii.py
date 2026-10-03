class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        freq={}
        for num in nums1:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        lst=[]
        for num in nums2:
            if num in freq and freq[num]>0:
                lst.append(num)
                freq[num]-=1
        return lst        
