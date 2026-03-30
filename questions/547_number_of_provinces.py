"""
Start: 15:20
End: 15:36

https://leetcode.com/problems/number-of-provinces/?envType=study-plan-v2&envId=leetcode-75

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b`
is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `i`th city and the `j`th city are directly connected,
and `isConnected[i][j] = 0` otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:

- 1 <= n <= 200
- n == isConnected.length
- n == isConnected[i].length
- isConnected[i][j] is 1 or 0.
- isConnected[i][i] == 1
- isConnected[i][j] == isConnected[j][i]

Questions / notes:
 - Max number of provindes is n? Yes, no connections
 - Symmetric: Yes

Notes
 - Worst case, have to visit N-1 nodes (last one would have been connected somewhere else)
 - Can traverse above or below diagonal, due to symmetry
 - Always self connected, 1s along diagonal
 

Options
 - Begin traversal w/ 0, 0
 - Container w/ seen indices. Container w/ indices to check. Whenever container is empty, increment number of provinces, find next unseen index

Notes for next time:
 - Swapped j, j_val on accident
 - For loop outside of while loop to keep track of unseen provinces. Can just skip if seen already
"""
from collections import deque
from typing import List
from unittest import TestCase


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = deque()
        v = set()
        s = 0

        for i in range(len(isConnected)):
            if i in v:
                continue
           
            d.append(i)
            v.add(i)
            
            while len(d) > 0:
                c = d.popleft()
                
                for j, j_val in enumerate(isConnected[c]):
                    if j_val > 0 and j not in v:
                        d.append(j)
                        v.add(j)
            s += 1
        return s





tc = TestCase()
tc.assertEqual(Solution().findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2)
tc.assertEqual(Solution().findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3)
tc.assertEqual(Solution().findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]), 1)

