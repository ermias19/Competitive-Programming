def Next_greater_element():
    nums1 = [2,1,3]
    nums2 = [2,3,1]
    stack = []
    dic = {}
    result=[]

    for i in range(len(nums2)):
        if  stack==[] or stack[-1] > nums2[i]:
            stack.append(nums2[i])
        else:
            while stack!=[] and (stack[-1] < nums2[i]):
                dic[stack.pop()]=nums2[i]
            stack.append(nums2[i])
    for j in nums1:
        if j in dic.keys():
            result.append(dic[j])
        else:
            result.append(-1)



    print(dic)
    print(result)


Next_greater_element()
