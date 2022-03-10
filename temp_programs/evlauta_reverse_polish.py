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