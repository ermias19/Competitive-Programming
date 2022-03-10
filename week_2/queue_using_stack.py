from collections import deque
class queue_stack():
    def __init__(self):
        self.stack1=[]
        self.stack2=deque()
    def push(self,value):
        self.stack1.append(value)
        while self.stack1!=[]:
            ermias=self.stack1.pop()

            self.stack2.appendleft(ermias)



    def peek(self):
        return self.stack2[-1]
        
    def pop(self):
        return self.stack2.pop()

    def empty(self):
        if  not self.stack2:
            return True
        else:
            return False

queue= queue_stack()
queue.push(2)



queue.pop()
print(queue.stack2)
print(queue.empty())