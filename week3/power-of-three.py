import math 
def powerofthree(n):
    if  n==1:
        return True
    else:
        if n%3!=0 or n==0:
            return False
    return powerofthree(n//3) 
print(powerofthree(9))