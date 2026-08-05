# class Solution:
#     def numTrees(self, n: int) -> int:
        # RECURSION 
        # if n <= 1 :
        #     return 1
        # if n == 2:
        #     return 2 
        # count = 0 
        # for root in range ( 1 , n+1 ):
        #     left  = self.numTrees(root - 1)
        #     right = self.numTrees(n - root)
        #     count += left * right 
        # return count 

        #  TABULATION 

class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] = Number of unique BSTs with i nodes
        dp = [0] * (n + 1)

        # Base cases
        dp[0] = 1
        dp[1] = 1

        # Fill DP table
        for nodes in range(2, n + 1):
            count = 0

            for root in range(1, nodes + 1):
                left = dp[root - 1]
                right = dp[nodes - root]

                count += left * right

            dp[nodes] = count

        return dp[n]