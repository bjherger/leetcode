"""
Start: 14:04
End: TODO

https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=study-plan-v2&envId=leetcode-75

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]

Example 3:

Input: root = [1,null,3]
Output: [1,3]

Example 4:

Input: root = []
Output: []

Constraints:

- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100

Questions / notes:
 - Is tree represented as custom node objects, or an array? Custom class
 - Breadth first right most only? yes
 - Nullable root? Yes

Options
 - O1: Brute force - convert to array, get each row's right most
 - O2: Breadth first search, append right most to results array. Can be done w/ either single queue keeping track of level and updating ith index, or two containers and updating when current container is of size 1

Notes for next time:
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        d = deque()
        if root is not None:
            d.appendleft((root, 0))
        r = list()

        while len(d) > 0:
            c, i = d.popleft()
            print(c, i)

            if c.left is not None:
                d.append((c.left, i + 1))
            
            if c.right is not None:
                d.append((c.right, i + 1))
            
            if i > len(r) -1:
                r.append(c.val)
            else:
                r[i] = c.val
        return r


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
tc.assertEqual(Solution().rightSideView(_build_tree([1, 2, 3, None, 5, None, 4])), [1, 3, 4])
tc.assertEqual(Solution().rightSideView(_build_tree([1, 2, 3, 4, None, None, None, 5])), [1, 3, 4, 5])
tc.assertEqual(Solution().rightSideView(_build_tree([1, None, 3])), [1, 3])
tc.assertEqual(Solution().rightSideView(_build_tree([])), [])

