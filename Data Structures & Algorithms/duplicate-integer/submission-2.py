class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force -- check every element against every other element in the array. This would be an O(n^2) solution.

        if len(set(nums)) != len(nums):
            return True
        else:
            return False

        