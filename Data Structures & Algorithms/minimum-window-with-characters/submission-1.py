class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # initialize two hashmaps, for HAVE vs NEED
        count_t, window = {}, {}

        # initialize the hashmap of the counts of characters in t
        for char in t:
            # if char exists in the hashmap, return the count. Otherwise return zero
            count_t[char] = 1 + count_t.get(char, 0)

        have, need = 0, len(count_t) # is this correct?

        res = [-1, -1] # left and right pointers
        res_len = float('infinity')
        left = 0

        for right in range(len(s)):
            cur_char = s[right]
            # update the window counts
            window[cur_char] = 1 + window.get(cur_char, 0)

            # is the current character in t at all?
            # does window of the current character satisfy condition?
            if cur_char in count_t and window[cur_char] == count_t[cur_char]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    # update our result
                    res = [left, right]
                    res_len = right - left + 1
                # pop from the left of our window
                window[s[left]] -= 1

                if s[left] in count_t and window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        final_left, final_right = res

        return s[final_left:final_right + 1] if res_len != float('infinity') else ""
        