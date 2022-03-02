# nums= [3,30,34,5,9]
nums=[0,0]
for i in range(len(nums)):
   
    for j in range(len(nums)):
       if str(nums[i])+str(nums[j])<str(nums[j])+str(nums[i]):
           nums[j],nums[i]=nums[i], nums[j]
        

nums.reverse()
if nums[0]==0:
    print("0")

print(nums)












# for i in range(len(nums)):
#             min_value=i
#             for j in range(i+1,len(nums)):
#                 if nums[min_value]>nums[j]:
#                     min_value=j
#             if min_value!=i:
#                nums[min_value], nums[i]= nums[i],nums[min_value]

# string_numbers=[str(ints) for ints in nums]
# splity="".join(string_numbers)
# print(splity)