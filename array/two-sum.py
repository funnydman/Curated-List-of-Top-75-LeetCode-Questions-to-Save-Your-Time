"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def two_sum(nums, target):
    table = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if nums[i] in table:
            return [i, table[nums[i]]]
        table[diff] = i


assert two_sum([-1, -2, -3, -4, -5], -8) == [4, 2]
assert two_sum([3, 2, 4], 6) == [2, 1]
assert two_sum([3, 3], 6) == [1, 0]
