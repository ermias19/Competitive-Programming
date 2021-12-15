class solution:
    def fizBuzz(self,n):
        list1=[]
        for i in range(1,n+1):
            # list1.append(i)
            if(i%3==0 and i%5==0):
                list1.append("FizzBuzz")
            elif(i%3==0):
                list1.append("Fizz")
            elif(i%5==0):
                list1.append("Buzz")
            else:
                list1.append(str(i))
        print(list1)
             

sol=solution()
sol.fizBuzz(15)
