class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hashmap to count occurences of each character
        count = {}
        res = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)

            # check if the current window is valid
            # window_len = right - left + 1
            # while the window is not valid, update the left pointer
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1 # decremenet the count of the character on the left
                left += 1

            res = max(res, right - left + 1)
        return res
