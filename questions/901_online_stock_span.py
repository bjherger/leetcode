"""
Start: 11:36
End: 11:58

https://leetcode.com/problems/online-stock-span/?envType=study-plan-v2&envId=leetcode-75

Design an algorithm that collects daily price quotes for some stock and returns the **span** of that stock's price for the current day.

The span of the stock's price in one day is the maximum number of consecutive days (starting from that day and going backward) for which the stock price was less than or equal to the price of that day.

For example, if the prices of the stock in the last four days are [7,2,1,2] and the price of the stock today is 2, then the span of today is 4 because starting from today, the price of the stock was less than or equal to 2 for 4 consecutive days.

Also, if the prices of the stock in the last four days are [7,34,1,2] and the price of the stock today is 8, then the span of today is 3 because starting from today, the price of the stock was less than or equal to 8 for 3 consecutive days.

Implement the `StockSpanner` class:

- `StockSpanner()` Initializes the object of the class.
- `int next(int price)` Returns the span of the stock's price given that today's price is `price`.

Example 1:

Input:
["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
[[], [100], [80], [60], [70], [60], [75], [85]]

Output:
[null, 1, 1, 1, 2, 1, 4, 6]

Explanation:
StockSpanner stockSpanner = new StockSpanner();
stockSpanner.next(100); // return 1
stockSpanner.next(80);  // return 1
stockSpanner.next(60);  // return 1
stockSpanner.next(70);  // return 2
stockSpanner.next(60);  // return 1
stockSpanner.next(75);  // return 4
stockSpanner.next(85);  // return 6

Constraints:

- 1 <= price <= 10^5
- At most 10^4 calls to `next` for each test case.
- At most 10^5 calls to `next` in total across all test cases.

Questions / notes:
 - Include today in span? Yes
 - <=. Yes

Options
 - BF: Add current day to list, compare current day against all preceeding days
 - Monotonic Stack: Stack contains strictly decreasingo values the further down you go. Sum number of equal or greater until value exceeds current value

Notes for next time:
"""

from collections import deque
from unittest import TestCase


class StockSpanner:
    def __init__(self) -> None:
        self.d = deque()

    def next(self, price: int) -> int:
        v, c = price, 1
        d = self.d
        
        while len(d) > 0 and d[-1][0] <= v:
            pv, pc = d.pop()
            c += pc
        d.append((v, c))
        return c


tc = TestCase()

# Example 1: [7,2,1,2] then 2 → span = 4
sp = StockSpanner()
tc.assertEqual(sp.next(7), 1)
tc.assertEqual(sp.next(2), 1)
tc.assertEqual(sp.next(1), 1)
tc.assertEqual(sp.next(2), 3)  # up to here
tc.assertEqual(sp.next(2), 4)  # today

# Example 2: [7,34,1,2] then 8 → span = 3
sp = StockSpanner()
tc.assertEqual(sp.next(7), 1)
tc.assertEqual(sp.next(34), 2)
tc.assertEqual(sp.next(1), 1)
tc.assertEqual(sp.next(2), 2)
tc.assertEqual(sp.next(8), 3)  # today