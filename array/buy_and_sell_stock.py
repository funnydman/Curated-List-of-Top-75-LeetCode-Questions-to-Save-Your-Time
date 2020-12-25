"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


def max_profit(prices) -> int:
    if not prices:
        return 0

    imi = ima = 0
    maximum = 0

    for i in range(len(prices)):
        if prices[i] <= prices[imi]:
            imi = ima = i

        if prices[i] > prices[ima]:
            ima = i
            maximum = max(maximum, prices[ima] - prices[imi])

    return maximum


assert max_profit([7, 1, 5, 3, 6, 4]) == 5
assert max_profit([7, 6, 4, 3, 1]) == 0
