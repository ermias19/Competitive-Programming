class NestedIterator:
    def __init__(self, nestedList):
        self.nestedList=nestedList
        # self.val=
    def list_str(self):
        stri=''
        for i in self.nestedList:
            if i != ',':
                stri+=str(i)
        # print('bla bla',type(i))
        return stri
    def iterator(self):
        string=NestedIterator.list_str(self)
        res=[]
        for i in string:
            # print(i)
            if not res:
                res.append(i)
                print(res)
            elif i==']':
                # print(i)
                while res=='[':
                    poped_val=res.pop()
                    res.append(poped_val)
                res.pop()
            elif i!=',':
                res.append(i)
            
            # res.append(self.nestedList)
            # elif res[0]=='[' and type(res[-1])is int:
            #     poped_val=self.nestedList.pop()
            #     res.append(poped_val)
        return res
                    
nested_list=[[1,1],2,[1,1]]
obj=NestedIterator(nested_list)
print(obj.iterator())

print((obj.list_str()))

# print(stri)
# print(''.join(str(list1)))
# print(''.join([str(elem) for elem in list1]))
