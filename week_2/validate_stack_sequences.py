from typing import *

def validateStackSequences(pushed: List[int], popped: List[int]) -> bool:
    popped.reverse()
    stack = []
    i =0
    while popped and i<len(pushed):
        current = popped[-1]
        while i<len(pushed) and current != pushed[i]:
            stack.append(pushed[i])
            i+=1
        print(stack, popped)
        
        if i< len(pushed):
            stack.append(pushed[i])
        else:
            break
        i+=1

        while len(popped) > 1 and stack and current == stack[-1]:
            a = stack.pop()
            # print(a)
            b = popped.pop()
            # print(b)
            current = popped[-1]
    print("final")
    print(stack, pushed, popped)
    return stack == popped                
