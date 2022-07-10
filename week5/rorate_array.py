
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums:List,beg:int, end:int):
            temp = 0
            while beg<end:
                temp = nums[beg]
                nums[beg]=nums[end]
                nums[end]=temp
                beg = beg +1
                end = end -1
        end =  len(nums)-1
        k = k%len(nums)
        if(len(nums)>1):
            reverse(nums,0,end)
            reverse(nums,0,k-1)
            reverse(nums,k,end)