class Solution:
    def isValid(self, s: str) -> bool:
        dict={'{':'}','(':')','[':']'}
        stack=[]
        for i in s:
            if i in dict.keys():
                stack.append(i)
            elif stack==[] or dict[stack.pop()]!= i:
                return False
        if len(stack)==0:
            return True
        return































# s = "(])"
# a = []
# booly = False
# is_empty = True
# c = 0
# for i in s:
#     print(i)
#     if i == "(" or i == "[" or i == "{" or a==[]:


#         a.append(i)
    
#     if a != []:
#         if   a[-1] == '[' and i == ']':
#             print('ermias', a)
#             a.pop()
           
#     if a == []:
#             is_empty = True
#     else:
#             is_empty = False
   
# if is_empty == False:
#     booly = False
# else:
#     booly=True
# print(booly)
# print(a)

#    if i=="(" or i=="[" or i=="{" :
#          a.append(i)
#    if i==")" or i=="]" or i=="}" :
#          if a[c]=="(" and i==")" or a[c]=="{" and i=="}" or a[c]=="[" and i=="]":
#              print(i)
#              a.pop()

#              booly=True
#              c+=1
#              print(c)
#    else:
#         booly=False

# b=s[slice(i)]
# print(b)
# if b=="(" or b=="[" or b=="{" :
#     a.append(b)
#     print(b,'b yihe new')
# if b==")" or b=="]" or b=="}" :
#     print('ahun demoo )}] nw',b)
#     print(a[i],'ermudaa')
#     if a[i]=="(" and b==")" or a[i]=="{" and b=="}" or a[i]=="[" and b=="]":
#         print(a,'ermas')
#         a.pop()
#         booly=True


# class Solution:
#     def isValid(self, s: str) -> bool:
#         dict={'{':'}','(':')','[':']'}
#         stack=[]
#         for i in s:
#             if i in dict.keys():
#                 stack.append(i)
#             elif stack==[] or dict[stack.pop()]!= i:
#                 return False
#         if len(stack)==0:
#             return True
#         return
