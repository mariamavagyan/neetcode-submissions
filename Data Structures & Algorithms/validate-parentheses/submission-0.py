class Solution:
    def isValid(self, s: str) -> bool:
        # Time complexity: O(n), Memory: O(n) due to the stack
        stack = []
        # make a hashmap where keys are the CLOSING parentheses
        closeToOpen = {")": "(",
                        "]":"[",
                        "}" : "{"}

        # go through each character
        for c in s:
            # if the character is in the hashmap, ie is a closing parenthesis
            if c in closeToOpen:
                # check if its corresponding value matches the top of the stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        # don't forget to check if the stack is empty. If nonemtpy, then return False
        return True if not stack else False




        