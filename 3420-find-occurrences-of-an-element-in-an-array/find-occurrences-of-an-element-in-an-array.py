class Solution:
    def occurrencesOfElement(self, nums, queries, x):
        positions = []

        for i in range(len(nums)):
            if nums[i] == x:
                positions.append(i)

        ans = []

        for q in queries:
            if q <= len(positions):
                ans.append(positions[q - 1])
            else:
                ans.append(-1)

        return ans