"""
Start: 14:01
End: 14:13

https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75

You are given two positive integer arrays spells and potions, of length n and m respectively,
where spells[i] represents the strength of the ith spell and potions[j] represents the strength
of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the
product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form
a successful pair with the ith spell.

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]

Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]

Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful.
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful.
Thus, [2,0,2] is returned.

Constraints:

- n == spells.length
- m == potions.length
- 1 <= n, m <= 10^5
- 1 <= spells[i], potions[j] <= 10^5
- 1 <= success <= 10^10

Questions / notes:
 -Unique strengths within potions / spells? No
 - Ordered: No
 - s = len(spells), p = len(potions)

Options
 - O1: Brute force, check each potion w/ each spell
  - T: O(s*p)
  - S: O(s)
 - O2: Sort potions, get upper and lower bound
   - T: O(plg(p) + nlg(p)) 
   - S: O(s) (if sorting potions in place)
 - O3: Counter for potions, determine how many potions have at least strength of X
   - Alot
 - O4: Counter of potions, loop through all potions each time
   - Rpoughly same as O1

Will use O2

Notes for next time:
 - + not max for Time complexity (is this right?)
 - bisect_left does heavy lifting
"""
from math import ceil
from typing import List
from unittest import TestCase

def num_matches(e, p, success):
    threshold = ceil(success / e)
    low = 0
    high = len(p)
    while low < high:
      mid = (low + high) // 2

      if p[mid] < threshold:
        low = mid + 1
      else:
        high = mid
    return len(p) - low

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        r = [0] * len(spells)
        for i, e in enumerate(spells):
            r[i] = num_matches(e, potions, success=success)
        return r


tc = TestCase()
tc.assertEqual(Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7), [4, 0, 3])
tc.assertEqual(Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16), [2, 0, 2])
