class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[float('inf')]*n
        dp[n-1]=0
        for i in range(n-2,-1,-1):
            steps=min(i+nums[i],n-1)
            # print(steps)
            for jump in range(i+1,steps+1):
                dp[i]=min(dp[i],1+dp[jump])
                # print(dp)
        return dp[0]