class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = [] # result should be a list of lists
        nums.sort()
        for i, a in enumerate(nums):
            # dont reuse the same value in the same position twice
            if i > 0 and a == nums[i-1]: # if it's not the first value in the array, and a is equal to the previous number
                continue # dont use the same value twice, continue to the next iteration of the loop
            # use Two Sum II
            left, right = i + 1, len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum <0:
                    left += 1
                else:
                    res.append([a, nums[left], nums[right]])
                    # update pointers
                    # [-2, -2, 0, 0, 2, 2]
                    # only need to update one pointer, the if conditions up there will update the other two pointers
                    left += 1

                    # we dont want to have the same sum, so let's use a loop
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res
        