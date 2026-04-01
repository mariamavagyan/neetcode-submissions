class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = 0

        for n in num_set:
            # check whether each number has a left neighbor
            if (n-1) not in num_set:
                # then this number is a start of a sequence
                l = 0 # let's start counting the length of this sequence
                while (n+l) in num_set:
                    # while the right neighbor is in the set, the sequence is consequtive
                    # continue counting its length
                    l += 1
                # once the sequence is over, let's compare its length to the longest one we had so far
                longest_seq = max(longest_seq, l)
        return longest_seq