class Solution:

    def encode(self, strs: List[str]) -> str:
        # encode all the strings, number of characters + # + the string
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # read character by character, decode each string
            # the first position is an integer
            j = i
            while s[j] != "#": # we are still at the integer character
                j += 1 # increment j by 1 until we find a poud character
            # once we get to the pound character
            length = int(s[i:j]) # this is the integer in a string format, let's convert it to an integer
            res.append(s[j+1 : j+1+length]) # append the string/entire word
            # now, go to the next word
            i = j + 1 + length
        return res


