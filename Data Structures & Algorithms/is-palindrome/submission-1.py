class Solution:
    def isPalindrome(self, s: str) -> bool:
        # # Solution 1
        # newStr = ""
        # # remove all non-alphanumeric characters
        # for c in s:
        #     if c.isalnum():
        #         newStr += c.lower() # convert to lowercase
        # # is it the same when it's reversed?
        # return newStr == newStr[::-1]

        # Soltuion 2
        l, r = 0, len(s) - 1

        while l < r:
            # make sure both characters at l and r are alphanumeric
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            # update pointers
            l += 1
            r -= 1
        return True

    def alphaNum(self, c):
        '''Check to see if the character is alphanumeric. Use ASCII values'''
        return (ord('A') <= ord(c) <= ord('Z') or # is it between A-Z?
        ord('a') <= ord (c) <= ord('z') or # is it between a-z?
        ord('0') <= ord(c) <= ord('9')) # is it between 0-9?
        # if yes, then it's alphanumeric!



        