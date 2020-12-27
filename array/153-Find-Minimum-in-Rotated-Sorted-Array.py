# modified binary search O(log(n))
class Solution:
    def findMin(self, nums):
        first = 0
        second = len(nums) - 1
        while first < second:
            mid = (first + second) // 2
            if nums[mid] > nums[second]:
                first = mid + 1
            else:
                second = mid
        return nums[first]
