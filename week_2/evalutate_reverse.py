import operator
def reverse_polish():
    tokens = ["0","3","/"]
    ops={"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
    stack=[]
    oprator='*/-+'
    for i in tokens:
        if i not in oprator:
            stack.append(i)
            
        else:
            elem1=stack.pop()
            elem2=stack.pop()
            elem1,elem2=int(elem1),int(elem2)
            result=ops[i](elem2,elem1)
            stack.append(result)
    print(int(stack[0]))
reverse_polish()



































# tokens = ["4","13","5","/","+"]

# stacK=[]

# ops='+*/-'

# for i in range(0,len(tokens),1):
#     a = b = 0
#     if tokens[i]not in ops:
#         stacK.append(int(tokens[i]))
#     elif tokens[i]=="+":
#         a=stacK.pop()
#         b=stacK.pop()
#         stacK.append(int(b)+int(a))
#     elif tokens[i]=="-":
#         a=stacK.pop()
#         b=stacK.pop()
#         stacK.append(int(b)-int(a))
#     elif tokens[i]=="*":
#         a=stacK.pop()
#         b=stacK.pop()
#         stacK.append(int(b)*int(a))
#     elif tokens[i]=="/":
#         a=stacK.pop()
#         b=stacK.pop()
#         stacK.append(int(int(b)/int(a)))
    
# print(stacK.pop())



