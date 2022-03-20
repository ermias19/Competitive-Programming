def devide_array():
    nums=[18,19,5,5,18,19,5,6,12,19,13,4,16,11,4,16,10,8,12,8,2,1,8,17,4,18,3,5,16,2,16,12,17,16,7,16,2,17,19,9,1,20,17,17,4,6]
    stack=[]
    a=True
    dic={}
    

    for i in nums:
        dic[i]=nums.count(i)
       
       
        if nums.count(i)%2==0:
            dic[i]=nums.count(i)
            print(i,a)
            print( nums.count(i))
            a=True
          
        else:
            return False
    return a


print(devide_array())










    # for i in nums:
    #     if not stack:
    #         stack.append(i)
    #     elif stack[-1]==i:
    #         stack.pop()
