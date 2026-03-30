"""
Start: 14:46
End: 14:55

https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

Given a binary tree `root`, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:

Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:

Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:

Input: root = [1]
Output: 1
Explanation: Root is considered as good.

Constraints:

- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].

Questions / notes:
 - > or >=: >=, can be good if element of equal value in path
 - Empty root: Won't happen
 - Number of good nodes, though location isn't important: No location requirement

Options
 - DFS or BFS, including largest value seen so far (node, max_so_far), does not include node.val in max_so_far

Notes for next time:
"""

from __future__ import annotations

from collections import deque
from typing import Optional, List
from unittest import TestCase


class TreeNode:
    def __init__(self, val: int = 0, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        d = deque()
        d.append((root, root.val))
        num_good = 0

        while len(d) > 0:
            c, msf = d.popleft()

            if c.val >= msf:
                num_good += 1

            if c.left is not None:
                d.append((c.left, max(msf, c.val)))

            if c.right is not None:
                d.append((c.right, max(msf, c.val)))
            
        return num_good


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
tc.assertEqual(Solution().goodNodes(_build_tree([3, 1, 4, 3, None, 1, 5])), 4)
tc.assertEqual(Solution().goodNodes(_build_tree([3, 3, None, 4, 2])), 3)
tc.assertEqual(Solution().goodNodes(_build_tree([1])), 1)

