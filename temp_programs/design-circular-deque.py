from collections import deque


class circular_deque:
    def __init__(self, k):
        self.queue = deque([])
        self.k = k
        self.front = 0
        self.rear = 0

    def insertFront(self, value):
        if  not self.isFull():
            self.queue.appendleft(value)
        else:
            return False

    def insertRear(self, value):
        if  not self.isFull():
            self.rear += 1
            self.queue.append(value)
        else:
            return False
    def getFront(self):
        if not self.isEmpty():
            return self.queue[0]
        else:
            return -1
    def getrear(self):
        if  self.isEmpty():
             return -1
            
        else:
           return self.queue[-1]

    def deleteFront(self):
        if not self.isEmpty():
            self.queue.popleft()
            return True

            
        else:
            return False
    def deleteRear(self):
        if not self.isEmpty():
            self.queue.pop()
            self.rear -= 1
        else:
            return False
    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False
    def isFull(self):
        if len(self.queue)==self.k:
            return True
        else:
            return False


obj = circular_deque(3)

obj.insertFront(4)
obj.deleteRear()
print(obj.isEmpty())
# obj.getrear()
# obj.deleteRear()
# obj.insertRear(2)
# obj.insertFront(3)
# obj.insertFront(4)
# print(obj.queue)
# print(obj.getrear())
# print(obj.isFull())
# obj.deleteRear()
# obj.insertFront(4)
# print(obj.getFront())

print(obj.queue)
