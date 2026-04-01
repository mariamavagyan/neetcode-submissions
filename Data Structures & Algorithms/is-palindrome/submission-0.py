class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Solution 1
        newStr = ""
        # remove all non-alphanumeric characters
        for c in s:
            if c.isalnum():
                newStr += c.lower() # convert to lowercase
        # is it the same when it's reversed?
        return newStr == newStr[::-1]
        