"""
Start: 14:25
End: 14:36

https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + (-8) = -1.
So we return the level with the maximum sum which is level 2.

Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

Constraints:

- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5

Questions / notes:
 - Nullable root? No

Options
 - Array w/ row's sum at that row's index
 - Iterate through each row, update result is > or no result yet
   - Same time complexity to traverse, space complexity is constant rather than h
 - Convert whole tree to array, sum up
 - Walk the whole tree to add to queue, then sum up (slower, no upside)

Will do 2

Notes for next time:
 - Row wise iteration w/ for loop isn't too bad. 
 - Tie breaking happens as expected
"""

from __future__ import annotations

from collections import deque
from typing import List, Optional
from unittest import TestCase


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        d = deque()
        d.append(root)
        result = None
        max_row = None
        current_row = 0

        while d:
            row_sum = 0
            current_row += 1
            for _ in range(len(d)):
                c = d.popleft()
                row_sum += c.val
                if c.left is not None:
                    d.append(c.left)
                if c.right is not None:
                    d.append(c.right)
            
            if result is None or row_sum > result:
                result = row_sum
                max_row = current_row

        return max_row

def _build_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    if not level_order:
        return None

    root_val = level_order[0]
    if root_val is None:
        return None

    root = TreeNode(root_val)
    q: deque[TreeNode] = deque([root])
    i = 1
    while q and i < len(level_order):
        node = q.popleft()

        if i < len(level_order):
            left_val = level_order[i]
            i += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                q.append(node.left)

        if i < len(level_order):
            right_val = level_order[i]
            i += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                q.append(node.right)

    return root


tc = TestCase()
tc.assertEqual(Solution().maxLevelSum(_build_tree([1, 7, 0, 7, -8, None, None])), 2)
tc.assertEqual(
    Solution().maxLevelSum(_build_tree([989, None, 10250, 98693, -89388, None, None, None, -32127])), 2
)

