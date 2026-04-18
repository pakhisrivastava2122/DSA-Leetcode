class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # s={}
        # for index , num in enumerate(nums):
        #     complement = target - num
        #     if complement in s:
        #         return [s[complement], index]
        #     s[num] = index
        # return []
        
        # BRUTE FORCE APPROACH  
        # n = len(nums)
       
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return([i,j])
            

# OPTIMAL APPROACHHH 
        n=len(nums)
        hash_set={}
        for i in range(0,n):
            remaining = target-nums[i]
            if remaining in hash_set:
                return [hash_set[remaining],i]
            hash_set[nums[i]]=i


                