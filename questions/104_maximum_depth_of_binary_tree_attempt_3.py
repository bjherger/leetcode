"""
Start: 14:36
End: 

https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100

Questions / notes:
 - Is tree represented as custom node objects, or an array? Custom class
 - Is root only depth 0 or depth 1? Depth 1
 - Can there be a row of only nulls (ie in array representation a row with no data?): No

Options
 - O1: Recursive, walk all branches, incrementing depth
 - O2: If stored as array, compute ceil(lg(len(n)) / lg(2))
 - O3: Convert whole thing to array, then do O2

Given that we have to touch ~all nodes anyways, O2 and O3 seem similar time complexity, but O3 requires additional space. Will do O1

Notes for next time:
 -
"""

from collections import deque
from typing import Optional
from unittest import TestCase


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    if values[0] is None:
        return None

    root = TreeNode(values[0])
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1

    return root


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        q = deque()
        q.append((root, 1))

        max_depth = 1

        while len(q) > 0:
            n, depth = q.pop()
            max_depth = depth if depth > max_depth else max_depth

            if n.left is not None:
                q.appendleft((n.left, depth + 1)) #Append left for BFS
                # q.append((n.left, depth + 1)) # Append right for DFS

            if n.right is not None:
                q.appendleft((n.right, depth + 1)) #Append left for BFS
                # q.append((n.right, depth + 1)) # Append right for DFS

        return max_depth
        


# Tests (from examples)
tc = TestCase()
root_1 = [3, 9, 20, None, None, 15, 7]
tc.assertEqual(Solution().maxDepth(list_to_tree(root_1)), 3)

root_2 = [1, None, 2]
tc.assertEqual(Solution().maxDepth(list_to_tree(root_2)), 2)

