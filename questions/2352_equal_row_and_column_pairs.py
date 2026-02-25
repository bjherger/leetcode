"""

Start: 10:19
End: 10:38

https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105

Questions / notes:
 - Empty matrix: 


Options
 - Option 1: Brute force. Check every column against every row
   - T: O(n3)
   - S: O(1)
   - Can we do better: Probably. Don't need location
 - Option 2: Column and row sets
   - T: O(n2)
   - S: O(n2)
   - Can we do better: Probably not?

Edge cases

 - Empty array
 - Everything matches

Notes

 - Time complexity was off. Why?
 - Originally used frozenset instead of tuple (frozen list), which caused slight issues
 
"""
from typing import List
from unittest import TestCase

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        matches = 0
        rows = dict()

        for i in grid:
            i = tuple(i)
            rows[i] = rows.get(i, 0) + 1
        
        for i in range(len(grid[0])):
            l = list()
            for j in grid:
                l.append(j[i])
            c = tuple(l)
            matches += rows.get(c, 0)

        return matches

# Tests
tc = TestCase()
s = Solution()

tc.assertEqual(
    s.equalPairs(
       grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
    )
    , 3
    )


tc.assertEqual(
    s.equalPairs(
        grid = [[3,2,1],[1,7,6],[2,7,7]]
    )
    , 1
    )