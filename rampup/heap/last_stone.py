import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for i in stones:
            heapq.heappush(h,(-i)) // Using as max heap.
        while(len(h)-1):
            x = heapq.heappop(h) // x and y are top 2 largest values.
            y = heapq.heappop(h)
            heapq.heappush(h,x-y)
        ans = heapq.heappop(h)
        return -ans