nums=[7,3,8,9,1,3,6]

for i in range(1,len(nums)):
    counter=i
    while nums[counter-1]<nums[counter] and counter>=0:
       nums[counter], nums[counter-1]= nums[counter-1],nums[counter]
       print(nums)
       counter-=1

 