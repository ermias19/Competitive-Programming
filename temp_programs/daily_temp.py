
def daily_temp():
    temperatures = [73,74,75,72,76,73]
  
    len_temp=len(temperatures)
    stack, result = [], [0]*len_temp
    dic = {}
    print(result)
    
    for i in temperatures:
        if not stack or stack[-1] > i:
            stack.append(i)
        else:
            counter = 0
            ermias=0
            while stack and stack[-1] < i:
                # print(temperatures.index(i),temperatures.index(stack[-1]))
                counter=temperatures.index(i)-temperatures.index(stack[-1])
                elem = stack.pop()
                print(temperatures.index(elem),elem,i)
                result[temperatures.index(elem)]=counter
                dic[counter] =  elem
            stack.append(i)
    
             

    print('this is dic', dic)
    print(result)


daily_temp()
