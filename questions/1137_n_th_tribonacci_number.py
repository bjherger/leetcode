"""
Start: 15:27
End: 15:37

https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=leetcode-75

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example 1:

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Example 2:

Input: n = 25
Output: 1389537

Constraints:

- 0 <= n <= 37
- The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

Questions / notes:
 -

Options
 - Keep list of numbers, sum up
   - T: O(n)
   - S: O(n)
 - Memoization: Hashmap w/ results, recursive calls
 - 3 pointers: Have array of length 3 and counter for current value of n. Sum, update array, and increment until we reach n
   - T: O(n)
   - S: O(1)

Notes for next time:
 -
"""

from unittest import TestCase


class Solution:
    def tribonacci(self, n: int) -> int:

        a = [0, 1, 1]
        c = 2

        if n <=2:
            return a[n]

        while c < n:
            hold = a[0] + a[1] + a[2]
            a[0], a[1], a[2] = a[1], a[2], hold
            c += 1
        return a[-1]

tc = TestCase()
tc.assertEqual(Solution().tribonacci(0), 0)
tc.assertEqual(Solution().tribonacci(1), 1)
tc.assertEqual(Solution().tribonacci(2), 1)
tc.assertEqual(Solution().tribonacci(4), 4)
tc.assertEqual(Solution().tribonacci(25), 1389537)
