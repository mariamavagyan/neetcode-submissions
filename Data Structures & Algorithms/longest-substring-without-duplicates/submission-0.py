class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()
        # Sliding window, need two pointers
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in char_set:#ie is duplicate
                # update the window via removing the character from the set
                char_set.remove(s[left])
                # update left pointer
                left += 1
            # add the rightmost character to our set
            char_set.add(s[right])
            # update the result
            cur_window_size = right - left + 1
            res = max(res, cur_window_size)
        return res
            
            


