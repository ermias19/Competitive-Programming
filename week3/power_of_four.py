def power_of_four(n):
    if n==1:
        return True 
    else:
        if n%4!=0 or n==0:
            return False
    return power_of_four(n//4)

print(power_of_four(16))



