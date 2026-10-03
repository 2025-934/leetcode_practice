class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq={}
        for word in strs:
            key="".join(sorted(word))
            if key not in freq:
                freq[key]=[]
            freq[key].append(word)
        return list(freq.values())