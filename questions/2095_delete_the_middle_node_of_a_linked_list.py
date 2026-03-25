"""

Start: 16:34
End: 16:47

https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing.

For example, if n = 1, 2, 3, 4, or 5, the middle nodes are at indices 0, 1, 1, 2, and 2, respectively.

Example 1:

Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation: The figure above represents the given linked list. The indices of the nodes are written below. Since n = 7, node 3 with value 7 is the middle node, which is marked in red. We return the new list after removing this node.

11
43
14
67

Example 2:

Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation: The figure above represents the given linked list. For n = 4, node 2 with value 3 is the middle node, which is marked in red.

11
32
4
Example 3:

Input: head = [2,1]
Output: [2]
Explanation: The figure above represents the given linked list. For n = 2, node 1 with value 1 is the middle node, which is marked in red. We return the new list after removing this node.

Constraints:

The number of nodes in the list is in the range [1, 10^5].
1 <= Node.val <= 10^5

Questions / notes:

 - Odd number: 3-> 1 removed
 - Even number: 4 -> 2 removed

Options

 - Option 1: Brute force: Walk entire list to get length. Walk from head again to (n/2) - 1, then remove middle element
   - T: O(n)
   - S: O(1) (assuming modify in place)
   - Critique: Correct and easy to get right. Two full passes (2n steps). Edge case: n=1 — middle is the only node, so return None; need an explicit check after the length pass (if n==1: return None) and then walk to the predecessor of the middle. Index of predecessor is ⌊n/2⌋ - 1; for n=1 that’s -1, so the “walk to predecessor” step doesn’t apply.
 - Option 2: Two pointers. Start both pointers at head. Move outer pointer 2x for every single movement of inner pointer. If outer pointer can only move once or out.next is None, remove the next element from the inner pointer
   - T: O(n)
   - S: O(1) (assuming modify in place)
   - Critique: One pass, so better constant factor. Wording is off: we don’t remove “when outer can only move once” — we remove when the fast pointer can’t advance two steps (fast.next is None or fast.next.next is None), and we must keep slow at the predecessor of the middle so we can rewire. Use a dummy node before head so deleting the first node (n=1) is the same as deleting any other: slow starts at dummy, fast at dummy; loop while fast.next and fast.next.next; then set slow.next = slow.next.next and return dummy.next. Fix typo: “singe” → “single”.

Notes for next time:
 - Use a 'dummy' head node ahead of the actual head node
 - Little bit of tricky handling w/ dummy head (ie remember to return next), evens and odds, etc
 - Doing a few by hand was helpful for figuring out when to actually move the inner

"""
from typing import Optional
from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1, next=head)
        inner = head
        outer = head
        while outer.next != None and outer.next.next != None:
            inner = inner.next
            outer = outer.next.next
        inner.next = inner.next.next
        return head.next


def list_from(vals: list[int]) -> Optional[ListNode]:
    """Build a linked list from a list of values."""
    if not vals:
        return None
    head = ListNode(vals[0])
    cur = head
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return head


def list_to(head: Optional[ListNode]) -> list[int]:
    """Convert a linked list to a list of values."""
    out: list[int] = []
    while head:
        out.append(head.val)
        head = head.next
    return out


# Tests
tc = TestCase()
s = Solution()
tc.assertEqual(list_to(s.deleteMiddle(list_from([1, 3, 4, 7, 1, 2, 6]))), [1, 3, 4, 1, 2, 6])
tc.assertEqual(list_to(s.deleteMiddle(list_from([1, 2, 3, 4]))), [1, 2, 4])
tc.assertEqual(list_to(s.deleteMiddle(list_from([2, 1]))), [2])
