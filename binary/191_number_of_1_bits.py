"""
https://leetcode.com/problems/number-of-1-bits/
"""
def hammingWeight(n):
    return bin(n)[2:].count("1")
        
