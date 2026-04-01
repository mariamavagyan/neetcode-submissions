import math
import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # output = np.zeros(n)
        # for i, n in enumerate(nums):
        #     print(f'i={i}, n={n}')
        #     output[i] = int(math.prod(nums) / nums[i])
        
        # return list(output)

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # store the prefix value
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix # multiply pre and post together
            postfix *= nums[i]
        return res
        