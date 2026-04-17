class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # s={}
        # for index , num in enumerate(nums):
        #     complement = target - num
        #     if complement in s:
        #         return [s[complement], index]
        #     s[num] = index
        # return []
        n = len(nums)
       
        for i in range(n-1):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return([i,j])
            




                