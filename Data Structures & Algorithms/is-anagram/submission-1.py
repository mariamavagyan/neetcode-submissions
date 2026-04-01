class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # brute force: sort both O(n log n), compare if they are equal. O(1) spacen n=len(s), m = len(t)
        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False

        # Frequency counter, count the requency for each letter, then compare them
        if len(s) != len(t):
            return False
        
        # create a dictionary for frequency counting
        d_s = {}
        for ch in s:
            if ch in d_s:
                d_s[ch] += 1
            else:
                d_s[ch] = 1
        
        # subtract from the frequency counter if a character is present.
        for ch in t:
            if ch in d_s:
                d_s[ch] -= 1
            else:
                # if not present, then not an anagram
                return False
        
        # if frequency is not zero, then not an anagram
        for c in d_s:
            if d_s[c] != 0:
                return False

        return True
    
        