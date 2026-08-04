# class Solution:
#     def thirdMax(self, nums: List[int]) -> int:
#         ans= nums.sort(reverse=True)
#         return ans[]
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) >= 3:
            return sorted(set(nums))[-3]
        else:
            return sorted(set(nums))[-1]