
class Stack(object):
    def __init__(self):
        self.item=[]
    def push(self,items):
        self.item.append(items)
    def pop(self):
        return  self.item.pop()
        
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None
    def isempty(self):
        if self.item==[]:
            return True
        else:
            return False
    def size(self):
        return len(self.item)
if __name__== "__main__":
    stack=Stack()
    stack.push('2')
    stack.push('44')
    print("the size is ",stack.size())
    print(stack.peek())
    print('------')
    print(stack.isempty())
    print(stack.pop())
    print(stack.peek())


