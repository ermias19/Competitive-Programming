def bubble_sortt():
    list1=[3,2,1]
    swap=0
    for i in range(len(list1)-1):
        for j in range(len(list1)-1):
            if list1[j]>list1[j+1]:
                list1[j], list1[j+1]=list1[j+1], list1[j]
                swap+=1
    print('Array is sorted in', swap, 'swaps.') 
    print('First Element:', list1[0])
    print('Last Element:', list1[-1])

bubble_sortt()