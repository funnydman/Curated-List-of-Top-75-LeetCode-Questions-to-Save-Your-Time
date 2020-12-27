class Solution:
    def productExceptSelf(self, nums):
        prod_below = [0] * len(nums)
        p = 1
        for i in range(len(nums)):
            prod_below[i] = p
            p *= nums[i]

        p = 1
        prod_above = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            prod_above[i] = p
            p *= nums[i]

        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prod_below[i] * prod_above[i]

        return res
