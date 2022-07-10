class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = "" #collect first number as string
        while l1 != None:
            n1 += str(l1.val)
            l1 = l1.next
        
        n2 = ""
        while l2 != None: #collect second number as string
            n2 += str(l2.val)
            l2 = l2.next
            
            
        res = str(int(n1[::-1])+int(n2[::-1])) #add both numbers and convert into string

        hd =None
        for i in range(len(res)): #create linked list again.
            hd = ListNode(int(res[i]),hd)

        return hd