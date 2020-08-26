from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


solution = Solution()
print(solution.singleNumber([2, 2, 1]))
