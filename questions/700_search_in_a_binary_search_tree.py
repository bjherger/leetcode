"""
Start: 14:58
End: 15:03

https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=study-plan-v2&envId=leetcode-75

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node.
If such a node does not exist, return `null`.

Example 1:

Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]

Example 2:

Input: root = [4,2,7,1,3], val = 5
Output: []

Constraints:

- The number of nodes in the tree is in the range [1, 5000].
- 1 <= Node.val <= 10^7
- root is a binary search tree.
- 1 <= val <= 10^7

Questions / notes:
 - Multiple matches? Won't happen
 - Empty tree? At least 1 node

Options
 - Traverse tree until we reach the node

Notes for next time:
 -
 
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
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        c = root

        while c is not None:

            v = c.val

            if v == val:
                return c
            elif val < v:
                c = c.left
            else:
                c = c.right

        return None


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


def _tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if root is None:
        return []

    out: List[Optional[int]] = []
    q: deque[Optional[TreeNode]] = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue

        out.append(node.val)
        q.append(node.left)
        q.append(node.right)

    while out and out[-1] is None:
        out.pop()
    return out


tc = TestCase()
tc.assertEqual(_tree_to_list(Solution().searchBST(_build_tree([4, 2, 7, 1, 3]), 2)), [2, 1, 3])
tc.assertEqual(_tree_to_list(Solution().searchBST(_build_tree([4, 2, 7, 1, 3]), 5)), [])

