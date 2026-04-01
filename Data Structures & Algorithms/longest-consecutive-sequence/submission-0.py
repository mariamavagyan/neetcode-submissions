class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_seq = 0

        # go thought every number in the array
        for n in nums:
            # check if it's the start of a sequence
            if (n-1) not in numSet:
                # then it is a start of a sequencey!
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest_seq = max(length, longest_seq)
        return longest_seq
        