class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        if self.stack:
            if self.min_stack:
                if self.min_stack[-1]<=val:
                    self.min_stack.append(self.min_stack[-1])
                elif self.min_stack[-1]>=val:
                    self.min_stack.append(val)
            else:
                 if self.stack[-1]<val:
                    self.min_stack.append(self.stack[-1])
                 elif self.stack[-1]>val:
                    self.min_stack.append(val)
        
        self.stack.append(val)
        
        
    
    def pop(self) -> None:
        print(self.min_stack)
        if self.min_stack:
            self.min_stack.pop()
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.stack)==1:
            return self.stack[-1]
        return self.min_stack[-1]
    
    
obj = MinStack()
obj.push(0)
obj.push(1)
obj.push(0)
obj.push(0)
obj.push(0)
print(obj.getMin())
# obj.pop()
print( obj.getMin())
# obj.push(-11)
# obj.push(-21)
# obj.pop()
param_3 = obj.top()


print('this is min stack',obj.min_stack)
print(obj.stack)
print(obj.min_stack)