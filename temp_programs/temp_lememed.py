def temp(n):
    n=str(n)
    le=len(n)
    # print(le)
    if le==0:
        return
    print(n[0]) 
    
    return temp(n[1:])
       
temp("ermias")