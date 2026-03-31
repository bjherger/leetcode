"""
Start: 12:56
End: TODO

https://leetcode.com/problems/non-overlapping-intervals/description/?envType=study-plan-v2&envId=leetcode-75

Given an array of intervals `intervals` where `intervals[i] = [starti, endi]`, return the minimum number of intervals you need to
remove to make the rest of the intervals non-overlapping.

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:

- 1 <= intervals.length <= 10^5
- intervals[i].length == 2
- -5 * 10^4 <= starti < endi <= 5 * 10^4

Questions / notes:

 - Intervals aren't inclusive of edges
 - Return number of intervals. Don't need to return specific intervals
 - Feels a bit like resolving a dependency tree

Options

 - Brute force: Compare every index with every other index. If two overlap, recursively remove one then the other and continue check
 - Iterate through, compare to seen intervals. If overlapping interval comes up, remove larger (doesn't guarantee smallest set)
 - Sort, iterate through and use heuristic to figure out which to remove
   - T: nlgn
   - S: C (if sort in place)


Notes for next time:
 - Seed current end w/ start of 0th, so 0th doesn't trigger
 - Handle current end diffrently for removed vs didn't
 - Not super intuitive that this guarantees minimum number of removed elements
"""

from typing import List
from unittest import TestCase


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <=1:
            return 0
        
        s = sorted(intervals, key= lambda x:x[0])
        
        ce = s[0][0]
        nr = 0

        for b,e in s:
            if b < ce:
                nr +=1
                ce = min(ce, e)
            else:
                ce = e

        return nr


tc = TestCase()
tc.assertEqual(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]), 1)
tc.assertEqual(Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]), 2)
tc.assertEqual(Solution().eraseOverlapIntervals([[1, 2], [2, 3]]), 0)

