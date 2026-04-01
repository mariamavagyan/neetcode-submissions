class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Brute force -- check every element against every other element in the array. This would be an O(n^2) solution. 
        n = len(nums)
        n_unique = len(set(nums))

        if n == n_unique:
            return False
        else:
            return True

        