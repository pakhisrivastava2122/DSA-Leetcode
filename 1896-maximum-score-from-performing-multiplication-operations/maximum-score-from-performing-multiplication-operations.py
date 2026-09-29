class Solution:
    def maximumScore(self, nums, multipliers):
        n = len(nums)
        m = len(multipliers)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for left in range(i, -1, -1):
                right = n - 1 - (i - left)

                take_left = (
                    nums[left] * multipliers[i]
                    + dp[i + 1][left + 1]
                )

                take_right = (
                    nums[right] * multipliers[i]
                    + dp[i + 1][left]
                )

                dp[i][left] = max(take_left, take_right)

        return dp[0][0]