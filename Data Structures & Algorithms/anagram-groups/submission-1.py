class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        # go through each string in the input
        for s in strs:
            # create a counter for character frequency, make this the key of the hashmap
            freq_count = [0] * 26 # 26 letters in the alphabet

            # go through each character in the string
            for c in s:
                idx = ord(c) - ord('a')
                freq_count[idx] += 1
            
            res[tuple(freq_count)].append(s)

        return list(res.values())

        
        