class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        first = 0
        second = len(height) - 1

        while first < second:
            min_line = min(height[first], height[second])
            max_area = max(min_line * (second - first), max_area)

            if min_line == height[first]:
                while min_line >= height[first] and first < second:
                    first+=1
            else:
                while min_line >=height[second] and first < second:
                    second-=1
        return max_area
