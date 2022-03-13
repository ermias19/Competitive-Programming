def reverse_string():
    s = "(ed(et(oc))el)"
    stack=[]
    temp_s=[]
    strf=""
    for i in s:
        if i==')':
            print(stack[-1])
            while stack[-1]!='(':
                print('ermulaa',stack)
                temp_s.append(stack.pop())
            stack.pop()
            ermias=temp_s[::-1]
            while len(ermias)!=0:
               stack.append(ermias.pop())
            temp_s=[]
        if i!=')':
            stack.append(i)
    strf="".join(stack)
    print(strf,'final stack nw yihge') 

reverse_string()