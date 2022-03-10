def valid_parenteses():
    s = "]"
    stack=[]
    parentheses={'{':'}','[':']','(':')'}
    opning=parentheses.keys()
   
   
    for i in s:
        if i in opning:
            stack.append(i)
            print((stack))
        elif stack==[] or  i in  parentheses[stack.pop()]:
            return False
    if not stack:
        return True
  

print(valid_parenteses())