class Node:
    def __init__(self, key, val, prev, next):
        self.frq = 0
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
class LFUCache:

    def __init__(self, capacity: int):
        self.max = capacity
        self.mfu = Node(None, None, None, None)
        self.lfu = Node(None, None, self.mfu, None)
        self.mfu.next = self.lfu
        self.map = {}
        self.frq_map ={}
        
    # utility functions (4 in number)
    def pop(self, n):
        n.prev.next = n.next
        n.next.prev = n.prev
        return n

    def push_in_front(self, n):
        self.mfu.next.prev = n
        n.next = self.mfu.next
        self.mfu.next = n
        n.prev = self.mfu
        return n
        
    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        node = self.map[key]
        self.frq_map[node.frq].remove(key)
        if len(self.frq_map[node.frq])==0:
            del self.frq_map[node.frq]
        node.frq += 1
        if node.frq in self.frq_map:
            self.frq_map[node.frq].append(key)
        else:
            self.frq_map[node.frq] =[]
            self.frq_map[node.frq].append(key)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.max ==0:
            return
        #print(self.map,self.frq_map)
        if key not in self.map:
            if len(self.map)==self.max:
                self.remove()
            node = Node(key, value, None, None)
            #print(node.key,node.frq)
            self.map[key] = self.push_in_front(node)
            node.frq += 1
            #print(node.frq,key)
            if node.frq in self.frq_map:
                self.frq_map[node.frq].append(key)
            else:
                self.frq_map[node.frq] =[]
                self.frq_map[node.frq].append(key)
            #print(self.frq_map)
        else:
            node = self.map[key]
            node.val = value
            self.frq_map[node.frq].remove(key)
            if len(self.frq_map[node.frq])==0:
                del self.frq_map[node.frq]
            node.frq += 1
            if node.frq in self.frq_map:
                self.frq_map[node.frq].append(key)
            else:
                self.frq_map[node.frq] =[]
                self.frq_map[node.frq].append(key)
                
    def remove(self):
        lfu = min(self.frq_map.keys())
        #print(lfu,self.frq_map)
        key = self.frq_map[lfu].pop(0)
        node = self.pop(self.map[key])
        del self.map[key]
        #print(self.frq_map,node.frq,key)
        if len(self.frq_map[node.frq])==0:
            del self.frq_map[node.frq]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)