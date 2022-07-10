class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums)%2==0:
            return True
        dp=[[0 for _ in range(len(nums))] for _ in range(len(nums)) ]
        for g in range(len(nums)):
            i=0
            for j in range(g,len(dp)):
                if g==0:
                    dp[i][j]=nums[i]
                elif g==1:
                    dp[i][j]=max(nums[i],nums[j])
                else:
                    val1=nums[i]+min(dp[i+2][j],dp[i+1][j-1])
                    val2=nums[j]+min(dp[i][j-2],dp[i+1][j-1])
                    dp[i][j]=max(val1,val2)
                i+=1
        player_1=dp[0][-1]
        s=sum(nums)
        player_2=s-player_1
        return player_1>=player_2