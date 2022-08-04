class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = nums
        heapq.heapify(self.queue)
        
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.queue, val)
        
        while len(self.queue) > self.k:
            heapq.heappop(self.queue)
            
        return self.queue[0]