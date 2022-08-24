class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.row,self.column=len(grid), len(grid[0])
        self.path=0
        self.result=[0]
        def max_area_island(r,c):
            # print(grid[r][c])
            if grid[r][c]==1:
                self.path+=1
                grid[r][c]=2
                if r>=1:max_area_island(r-1,c)
                if r<self.row-1:max_area_island(r+1,c)
                if c>=1:max_area_island(r,c-1)
                if c<self.column-1:
                    
                    max_area_island(r,c+1)
                
                self.result.append(self.path)
                self.path=0


            

        for inner_row  in range(self.row):
            for inner_column in range(self.column):
                # if grid[inner_row][inner_column]:
                max_area_island(inner_row,inner_column)
        # print(grid)
        # print(result)
        print(self.result)
        max_grid=max(self.result)
        return max_grid
            
            
                
        # max_area_island(self.row,self.column,[])
        # return self.counter
        