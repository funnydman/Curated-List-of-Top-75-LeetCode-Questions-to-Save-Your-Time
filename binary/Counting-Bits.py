"""
Simple ways to solve the same problem:
https://leetcode.com/problems/counting-bits/discuss/415257/Easy-Even-Odd-method-C%2B%2B-DP-solution
https://leetcode.com/problems/counting-bits/discuss/79545/easy-understanding-4-lines-python-solution-98-defeat
https://leetcode.com/problems/counting-bits/discuss/79557/How-we-handle-this-question-on-interview-Thinking-process-%2B-DP-solution
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]*(num + 1)
        for n in range(1, num+1):
            res[n] = res[n >> 1] + (n & 1)
        return res
