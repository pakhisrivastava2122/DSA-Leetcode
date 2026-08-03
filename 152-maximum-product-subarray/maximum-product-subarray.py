class Solution(object):
    def maxProduct(self, nums):
        max_product = nums[0]
        min_product = nums[0]
        ans = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i] < 0 :
                max_product , min_product = min_product , max_product
            
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i] , min_product * nums[i])

            ans = max(ans , max_product)
        return ans 


        """
        :type nums: List[int]
        :rtype: int
        """
        