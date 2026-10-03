class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq={}
        for i in arr:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1 
        lst=[]
        for val in freq.values():
            lst.append(val)
        if len(lst)==len(set(lst)):
            return True
        else:
            return False