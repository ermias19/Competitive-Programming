class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        while n!=1:
            s=s+"1"+''.join(reversed(['1' if i=='0' else '0' for i in s]))
            n-=1
        
        return s[k-1]

















# def find_kth_bit(n,k):
#     s="0"
    
#     if n==1:
#         s=s+"1"+''.join(reversed(['1' if i=='0' else '0' for i in s]))
#         return s
#     else:
#         print( s)
    
#     find_kth_bit(n-1,k)

# print(find_kth_bit(3,1))