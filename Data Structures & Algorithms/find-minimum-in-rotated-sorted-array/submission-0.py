class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # arbitrary default value
        l, r = 0, len(nums) - 1 # define two pointers

        # run binary search
        while l <= r:
            if nums[l] < nums[r]: # if we are in a sub-array that's already sorted
                res = min(res, nums[l])
                break
            m = (l + r ) // 2
            res = min(res, nums[m])
            # then, should we search to the left or to the right? Let's see:
            if nums[m] >= nums[l]:
                # we are in the left section. Move the left pointer!
                l = m + 1
            else:
                # we are in the right section. Move the right pointer!
                r = m - 1
        return res

