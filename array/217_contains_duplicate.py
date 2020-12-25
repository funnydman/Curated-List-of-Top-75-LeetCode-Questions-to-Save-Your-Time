"""
https://leetcode.com/problems/contains-duplicate/
"""


def contains_duplicate(nums):
    table = {}
    for i in range(len(nums)):
        if nums[i] in table:
            return True

        table[nums[i]] = 1

    return False


assert contains_duplicate([1, 2, 3, 4]) is False
assert contains_duplicate([1, 2, 3, 4, 1]) is True
