def power_three(n):
    if n==1 :
        return True 
    elif n%3!=0 or n==0:
        return  False
    return power_three(n//3)
       

        
   




print(power_three(9))


































# import math 
# def powerofthree(n):
#     if  n==1:
#         return True
#     else:
#         if n%3!=0 or n==0:
#             return False
#     return powerofthree(n//3) 
# print(powerofthree(9))