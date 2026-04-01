"""
Start: 10:54
End: 11:32

https://leetcode.com/problems/daily-temperatures?envType=study-plan-v2&envId=leetcode-75

Given an array of integers `temperatures` represents the daily temperatures, return an array `answer` such that `answer[i]` is the
number of days you have to wait after the `i`th day to obtain a warmer temperature. If there is no future day for which this is
possible, keep `answer[i] == 0` instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:

- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100

Questions / notes:
 - Last day will always be 0? Yes
 - Ties? Tie is not warmer

Options
 - Brute force: Compare eery index to all following temps
   -  Can we do better? Probably by pre-computing in some way
    - Would computing backwards help?
    - Would a stack of some sort help
 - Monotic stack: (From chat gpt hint): Stack has temps, strictly decreasing. When the cursor is greater than the hottest day in the stack (index 0), resolve
   - T: O(N)
   - S: O(N)

Notes for next time:
 - Didn't get the intution, even after hint. Solved w/ ChatGPT and then implemented to confirm
 - Concept - stack has days that get progressively cooler. Whenever the cursor is hotter, cursor's index is the answer for all of those indices
 - Should be a stack, not a queue
 - Logic isn't super complicated. Keep a stack where further left is always colder. If current date is warmer than top of stack, just start removing
"""

from collections import deque
from typing import List
from unittest import TestCase


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) < 1: 
            return []
        elif len(temperatures) == 1:
            return [0]
        
        d = deque()
        a = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            
            while len(d) > 0 and temperatures[d[-1]] < t:
                ji = d.pop()
                a[ji] = i - ji

            d.append(i)
                
        return a



tc = TestCase()
tc.assertEqual(
    Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
    [1, 1, 4, 2, 1, 1, 0, 0],
)
tc.assertEqual(Solution().dailyTemperatures([30, 40, 50, 60]), [1, 1, 1, 0])
tc.assertEqual(Solution().dailyTemperatures([30, 60, 90]), [1, 1, 0])
