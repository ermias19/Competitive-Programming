from collections import deque

from soupsieve import iselect
class mycircle:
    def __init__(self,k):
        size=k
        self.queue=deque([0] *size)
        self.front=0
        self.rear=0
        self.k=k
    def insertfront(self,value):
        
        if self.isEmpty():
           self.queue[self.front]=value
           return True
        
        if(((self.rear+1)%self.k)==self.front):
                return False
        
        else:
            self.front=(self.front-1)%self.k
            self.queue[self.front]=value
            self.rear=((self.rear+1)%self.k)
            return True  
    def insertlast(self,value):
        if(self.isEmpty()  ):
            self.queue[self.rear]=value
            return True
        elif(((self.rear+1)%self.k)!=self.front):
             self.rear=(self.rear+1)%self.k
             self.queue[self.rear]=value
             return True
            
        else:
           return False
           
    def deletfront(self):
       if not self.isEmpty():
           self.queue[self.front]=0
           if self.size!=1:
               self.front=(self.front+1)%self.k
            
        
        else:
            self.queue.remove(self.queue[self.front])
            self.queue[self.front]=0
            if self.queue[self.front+1]!=0:
                self.front+=1
            return True
    def delete_rear(self):
        if (self.front==-1 and self.rear==-1):
            return False
        # if((self.rear+1)%self.k==self.front):
        #     return False
        else:
           self.queue.remove(self.queue[self.rear])
           self.rear-=1
           return True
    def getfront(self):
        if (self.front==-1 and self.rear==-1):
            return False
        else:
            return self.queue[self.front]
    def getrear(self):
         if (self.front==-1 and self.rear==-1):
            return False
         else:
             return self.queue[self.rear]

    def isEmpty(self):
        
        if ((self.rear+1)%self.k):
            return False
        else:
            True 
    def isFull(self):
        # obj.queue.pop()
        if ((self.rear+1)%self.k==self.front):
            return True
        else:
            return False




            

obj= mycircle(3)
# obj.queue.pop()
# insert=obj.insertfront(5)
# getfont=obj.getfront()
# isempty=obj.isEmpty()
# deletefront=obj.deletfront()
insertlast=obj.insertlast(1)
insertlast=obj.insertlast(2)
insertlast=obj.insertfront(3)
# insert=obj.insertfront(77)





# print(isempty)
# print(getfont)

print(obj.front,obj.rear)

print(obj.queue)
# print('inser last',insertlast)
