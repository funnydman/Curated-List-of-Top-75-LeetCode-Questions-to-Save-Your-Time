# "pythonic solution", or it's better to you popcount in Python 3.9
def hammingWeight(n):
    return bin(n)[2:].count("1")


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            if (n & 1):
               res +=1
            n = n>>1
        return res
        
        
