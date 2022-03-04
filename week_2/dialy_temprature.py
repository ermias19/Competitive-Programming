class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []
        
        for curr_day, curr_temp in enumerate(temperatures):
        
            while stack and temperatures[stack[-1]] < curr_temp:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        
        return answer



























# temperatures = [73,74,75,71,69,76,72,73]
# stack=[]
# size=0
# sizearray=[[0]*len(temperatures)]
# stack.append(temperatures[0])
# for i in range(1,(len(temperatures))):
   
#     size+=1
#     if stack[-1]<temperatures[i]:
#         stack.append(temperatures[i])
#         sizearray[i]=(size)
#         stack.append(temperatures[i])
#         size=0
#     else:
#         size.append(0)
    

#     # elif temperatures[i]


    



