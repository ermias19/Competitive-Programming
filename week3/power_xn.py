class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x**n
        else:
            result=x**n
            return result
        return self.myPow(x,n-1)
        