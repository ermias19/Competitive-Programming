class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid)-1, 0
        length=-1
        count=0
        while m>=0 and n<len(grid[0]):
            if grid[m][n]<0:
                count+=len(grid[0])-n
                m-=1
            else:
                n+=1
        return count