"""
Start: 12:38
End: 12:54

https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array `nums`, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor
that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.

Constraints:

- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i.

Questions / notes:
 - Edges - always lower
 - Can't sort n log n
 - Ties / multiple peaks - any
 - Return index number, not value
 - Empty array - won't happen
 - Array of 1 - index 0

Options
 - Brute force - 3 pointers. Fails lg(n) requirement
 - Go uphill - start in the middle. If peak, end. If not peak, move uphill
   - T: O(lg n)
   - S: O(1)

Notes for next time:
 - Bug confusing ci and cv
 - Bug for left edge >. Should have used >=
 - Honestly, I probably wouldn't have been able to guess at the lg n solution by myself. It didn't feel super intuitive.
"""

from typing import List
from unittest import TestCase


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        ci = len(nums) // 2

        while True:

            cv = nums[ci]
            lv = nums[ci-1] if ci-1 >= 0 else cv - 1
            rv = nums[ci+1] if ci+1 < len(nums) else cv - 1

            if cv > lv and cv > rv:
                return ci
            elif lv > cv and ci-1 >= 0: 
                ci = ci - 1
            elif rv > cv and ci+1 < len(nums):
                ci = ci + 1


tc = TestCase()
tc.assertEqual(Solution().findPeakElement([1, 2, 3, 1]), 2)
tc.assertIn(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]), {1, 5})
tc.assertIn(Solution().findPeakElement([325]), {0})
tc.assertIn(Solution().findPeakElement([2, 1]), {0})

