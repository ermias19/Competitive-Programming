class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        st, res = [], [-1] * len(nums1)
        for n in nums2:
            while st and st[-1] < n:
                mp[st.pop()] = n
            st.append(n)
        
        for idx, num in enumerate(nums1):
            res[idx] = mp[num] if num in mp else -1
        
        return res



















# nums1 = [2,4]
# nums2 = [1,2,3,4]
# stack=[]
# dic={}
# dic2={}

# stack.append(nums2[0])
# for i in range(len(nums2)-1):
#     if nums2[i]>=nums2[i+1]:
#         stack.append(nums2[i+1])
#     else:
#         for j in range(len(nums2)):
#             elem=stack.pop()
#             print(elem,nums2[i+1])
#             dic.update({elem:nums2[i+1]})
#             if not stack:
#                 stack.append(nums2[i+1])
# if stack:
#     for k in range(len(stack)):
#         elem_stack=stack.pop()
#         dic.update({elem_stack:-1})
# for i in range(len(nums1)):
#     print('ermias',dic[nums1[i]])
#     stack.append(dic[nums1[i]])    




print(dic)


print(stack)


































# nums1=[2,1,3]
# nums2=[2,3,1]
# greater_num=[]
# gr=[-1]
# for i in range(len(nums1)):
#     for j in range(len(nums2)):
#         if nums1[i]==nums2[j]:
#             if nums2.index(nums2[j])==len(nums2)-1:
#                 greater_num.append(-1)

#             elif nums1[i]==nums2[j]:
#                 for k in range(j,len(nums2)):
#                     print(k)
#                     if nums2.index(nums2[k])==len(nums2)-1:
#                         gr[0]=gr[0]=-1
#                     elif nums2[k]<nums2[k+1]:
#                         print(nums2[k+1])
#                         gr[0]=nums2[k+1]
#                         break
                    
#                 greater_num.append(gr[0])
#             else:
#                     greater_num.append(-1)
                


        

# print(greater_num)