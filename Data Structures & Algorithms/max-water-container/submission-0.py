class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # # Brute force O(n^2)
        # res = 0
        # for left in range(len(heights)):
        #     for right in range(left +1, len(heights)):
        #         area = (right - left) * min(heights[left], heights[right])
        #         res = max(area, res)

        # return res

        # Two pointers, O(n)
        res = 0
        left = 0
        right = len(heights) - 1 # to maximize the area!
        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            res = max(res,  area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return res


        