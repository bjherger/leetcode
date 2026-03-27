"""
Start: 12:59
End: 13:17

https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Example 1:

Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true

Example 2:

Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false

Constraints:

- The number of nodes in each tree will be in the range [1, 200].
- Both of the given trees will have values in the range [0, 200].

Questions / notes:
 - Can they both be members of the share tree (e.g. one is parent of other, both share a parent?): Maybe
 - Order matters? Yes
 - Are trees stored as array? No, custom object

Options
 - O1: Walk both at the same time - difficult
 - O2: Walk both, save results, compare results
 - O3: Walk first, compare second results in order
    - Saves some memory, increases complexity
    - T: O(n+m)
    - S: O(L1 + L2)
    - Optimizaiton: Stop early if b has more leaves than a

DFS, to get leaves in order

Notes for next time:
 - Small bug in implementation, copied and pasted left is none logic, didn't full update to right
 - Small bug, need to add right leaf to the head of the deque before adding the left, to maintain left traversal before right
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

def tree_to_leaves(root: Optional[TreeNode]):
    if root is None:
        return []

    d = deque()
    d.append(root)

    leaves = list()

    while len(d) > 0:
        c = d.popleft()
        
        if c.right is not None:
            d.appendleft(c.right)
        if c.left is not None:
            d.appendleft(c.left)
        
        if c.left is None and c.right is None:
            leaves.append(c.val)

    return leaves

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        return tree_to_leaves(root1) == tree_to_leaves(root2)


# Tests (from examples)
tc = TestCase()
root1_ex1 = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
root2_ex1 = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
tc.assertEqual(Solution().leafSimilar(list_to_tree(root1_ex1), list_to_tree(root2_ex1)), True)

root1_ex2 = [1, 2, 3]
root2_ex2 = [1, 3, 2]
tc.assertEqual(Solution().leafSimilar(list_to_tree(root1_ex2), list_to_tree(root2_ex2)), False)

root1_ex3 = [1, 2]
root2_ex3 = [2, 1]
tc.assertEqual(Solution().leafSimilar(list_to_tree(root1_ex3), list_to_tree(root2_ex3)), False)
