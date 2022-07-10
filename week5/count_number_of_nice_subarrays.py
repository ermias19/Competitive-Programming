class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prev_start, prev_end = 0, 1
        odd_cnt = 0
        ret = 0
        for i, n in enumerate(nums):
            if n % 2 == 1:
                odd_cnt += 1
                while odd_cnt > k:
                    if nums[prev_start] % 2 == 1:
                        odd_cnt -= 1
                    prev_start += 1
                prev_end = prev_start
                add_back = False
                while odd_cnt > k - 1:
                    if nums[prev_end] % 2 == 1:
                        odd_cnt -= 1
                        add_back = True
                    prev_end += 1
                if add_back: odd_cnt += 1
            if odd_cnt == k:
                ret += (prev_end - prev_start)
        return ret