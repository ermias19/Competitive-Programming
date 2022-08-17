from heapq import heappush, heappop, heapify
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        minHeap = []
        heapify(minHeap)
        headNode = pointNode = ListNode(0)
        
        for i in lists:
            while(i!=None):
                heappush(minHeap,i.val)
                i=i.next
      
        while(len(minHeap)>0):
            pointNode.next=ListNode(heappop(minHeap))
            pointNode = pointNode.next
        return headNode.next