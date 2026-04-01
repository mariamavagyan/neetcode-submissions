class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count the frequencies
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        print(f'count = {count}')
        # 2. Build frequency buckets
        freq = [[] for i in range(len(nums)+1)]
        print(f'len(freq) = {len(freq)}')

        for n, c in count.items():
            freq[c].append(n)
        
        # 3. Count backwards to get top k
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        