from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        #initialize capacity
        self.capacity=capacity

    def get(self, key: int) -> int:
        # if key exist, move to the start of dict and return it
        if key in self:
            self.move_to_end(key, False)
            return self[key]
        # otherwise -1
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        # if capacity full, pop from last of dict
        if self.capacity== len(self) and key not in self:
            self.popitem(last=True)
        # update value or insert if key doesnt exist before
        self[key]=value
        # move to the start of dict
        self.move_to_end(key, False)  