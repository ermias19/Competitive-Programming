import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}
        heap = []
        
        for word in words:
            counter[word] = counter.get(word, 0) + 1
            
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
            
        return result