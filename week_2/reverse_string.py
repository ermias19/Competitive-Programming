from collections import deque
s = "(ed(et(oc))el)"
opining = '('
closing=')'
stack1 = []
qeue=deque()

stack2 = []

for i in range(len(s)):
    if s[i] != closing:
        stack1.append(s[i])
      
    else:
        while stack1 and  stack1[-1] != '(':
            qeue.append(stack1.pop(-1))
        stack1.pop(-1)
        while qeue:
            stack1.append(qeue.appendleft())

    
print(stack1)    

    # for i in range(len(stack2)):
    #     stack1.append(stack2.pop())


# for j in range(len(stack1)):
#     poped=stack1.pop()
#     stack2.append(poped)
# stack2= "".join(stack2)

# print(stack2)
# print('stack1',stack1)
