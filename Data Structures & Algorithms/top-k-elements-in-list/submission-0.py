class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            # print(f'count.get(n, 0)={count.get(n, 0)}')
            count[n] = 1 + count.get(n, 0) # if the dictionary contains n, return n, if not, return 0
        
        for n, c in count.items():
            freq[c].append(n) # value n occurs c number of times
        
        res = []
        # iterate in descending order
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: # for every value at index i
                res.append(n) #n appears most frequently
                if len(res) == k:
                    return res
        
