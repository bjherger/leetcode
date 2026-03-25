"""

Start: 15:57
End: 15:59

https://leetcode.com/problems/reverse-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is in the range [0, 5000].
-5000 <= Node.val <= 5000

Questions / notes:

 - Can val be null? No
 - Can head be null? Yes

Options

 - 

Notes for next time:

 - Pretty straight forward
 - Which pointer gets returned? the current pointer, which is the latest (last element)
 - Special case handling for if head or next are None
 - Make updates, update place holders
 - Can we get away with >4 pointers / variables?

"""
from typing import Optional
from unittest import TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = None
        c = head

        while c:
            n = c.next
            c.next = l

            l = c
            c = n

        return l

def list_from(vals: list[int]) -> Optional[ListNode]:
    """Build a linked list from a list of values."""
    if not vals:
        return None
    h = ListNode(vals[0])
    cur = h
    for v in vals[1:]:
        cur.next = ListNode(v)
        cur = cur.next
    return h


def list_to(head: Optional[ListNode]) -> list[int]:
    """Convert a linked list to a list of values."""
    out: list[int] = []
    while head:
        out.append(head.val)
        head = head.next
    return out


tc = TestCase()
s = Solution()
tc.assertEqual(list_to(s.reverseList(list_from([1, 2, 3, 4, 5]))), [5, 4, 3, 2, 1])
tc.assertEqual(list_to(s.reverseList(list_from([1, 2]))), [2, 1])
tc.assertEqual(list_to(s.reverseList(list_from([]))), [])
