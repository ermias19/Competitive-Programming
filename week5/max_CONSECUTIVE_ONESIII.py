class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        windowStart = 0
        max_length = 0
        max_ones_count = 0
        
        for windowEnd in range(len(nums)):
            if nums[windowEnd] == 1:
                max_ones_count += 1
                
            if(windowEnd - windowStart + 1 - max_ones_count) > k:
                if nums[windowStart] == 1:
                    max_ones_count -= 1
                windowStart += 1
            max_length = max(max_length,windowEnd - windowStart + 1)
        return max_length