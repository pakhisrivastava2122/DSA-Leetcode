class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #LINEAR SEARCH APPROACH
        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i 
        # return -1

        # BINARY SEARCH ALGORITHM 
        n=len(nums)
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1