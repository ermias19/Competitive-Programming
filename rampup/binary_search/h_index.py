class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result=[]
        def binary_search(nums,target):
            low,high=0,len(nums) - 1
            while low<=high:
                mid=(low+high)//2
                if nums[mid]<target:
                    low=mid+1
                elif nums[mid]>=target:
                    high=mid-1
            return low
        
        low=binary_search(nums,target)
        high=binary_search(nums,target+1)-1
        if high>=low:
            return [low,high]
        else:
            return [-1,-1]
                