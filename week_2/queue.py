class queue:
    def __init__(self):
        self.queue=[]

    def push(self,x):
        return self.queue.append(x)
    
    def pop(self):
        return self.queue.pop(0)

    def peek(self):
        lenqueue= len(self.queue)
        return self.queue[lenqueue-1]
    
    def empty(self):
        if self.queue==[]:
            return True
    
    










































#  class MyQueue:

#     def __init__(self):
#         self.s1 = []
#         self.s2 = []
#     def push(self, x: int) -> None:
        
#         self.s1.append(x)

#     def pop(self) -> int:
#         if len(self.s2) == 0:
#             while len(self.s1) > 0:
#                 self.s2.append(self.s1.pop())
#         return self.s2.pop()

#     def peek(self) -> int:
#         if len(self.s2) == 0:
#             while len(self.s1) > 0:
#                 self.s2.append(self.s1.pop())
#         return self.s2[-1]

#     def empty(self) -> bool:
#         return len(self.s1) == 0 and len(self.s2) == 0
        


# obj = MyQueue()
# obj.push(5)
# obj.push("MyQueue")
# obj.push("push")
# obj.push("pop")
# obj.push("peek")
# obj.push("empty")
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
        


# # Your MyQueue object will be instantiated and called as such:
# # obj = MyQueue()
# # obj.push(x)
# # param_2 = obj.pop()
# # param_3 = obj.peek()
# # param_4 = obj.empty()