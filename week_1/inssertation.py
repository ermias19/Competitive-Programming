arr=[78,8,48,6,5]

for i in range(1,len(arr)):
    counter=i
    while arr[counter]<arr[counter-1] and counter>0:
        arr[counter],arr[counter-1]=arr[counter-1],arr[counter]
        counter-=1

print(arr)
