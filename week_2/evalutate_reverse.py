

tokens = ["4","13","5","/","+"]

stacK=[]

ops='+*/-'

for i in range(0,len(tokens),1):
    a = b = 0
    if tokens[i]not in ops:
        stacK.append(int(tokens[i]))
    elif tokens[i]=="+":
        a=stacK.pop()
        b=stacK.pop()
        stacK.append(int(b)+int(a))
    elif tokens[i]=="-":
        a=stacK.pop()
        b=stacK.pop()
        stacK.append(int(b)-int(a))
    elif tokens[i]=="*":
        a=stacK.pop()
        b=stacK.pop()
        stacK.append(int(b)*int(a))
    elif tokens[i]=="/":
        a=stacK.pop()
        b=stacK.pop()
        stacK.append(int(int(b)/int(a)))
    
print(stacK.pop())



