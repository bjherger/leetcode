"""
Start: 14:55
End: 15:09

https://leetcode.com/problems/smallest-number-in-infinite-set/description/?envType=study-plan-v2&envId=leetcode-75

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

- SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
- int popSmallest() Removes and returns the smallest integer contained in the infinite set.
- void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.

Constraints:

- 1 <= num <= 1000
- At most 1000 calls will be made in total to popSmallest and addBack.

Questions / notes:
 -

Options
 - O1: Brute force - create an array up to max int
 - O2: Dual data structure - head containing the current head of the "infinite set", starting w/ 1, and min heap containing numbers added back in
 - O3: Dual data strucutre - head containing the current head of the "infinite set", and an array or hash map. Still need to iterate through all to find min to remove
 - O3: Dual data strucutre - head containing the current head of the "infinite set", and an BST. Adds runtime complexity for remove, add

 Will proceed with option 2

Notes for next time:
 - Minor bug in addBack, where > instead of >= min infinite number
 - There must be a better way to check if the number is in the heap already that checking the list or keeping a whole separate set
"""

from cgitb import small
from unittest import TestCase

import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.min_infinite_number = 1
        self.h = list()
        self.s = set()

    def popSmallest(self) -> int:
        if len(self.h) < 1 or self.h[0] > self.min_infinite_number:
            self.min_infinite_number += 1
            return self.min_infinite_number -1
        else:
            smallest = heapq.heappop(self.h)
            self.s.remove(smallest)
            return smallest

    def addBack(self, num: int) -> None:
        if num >= self.min_infinite_number:
            return

        if num in self.s:
            return
        
        heapq.heappush(self.h, num)
        self.s.add(num)


# Tests (from Example 1)
tc = TestCase()
s = SmallestInfiniteSet()
s.addBack(2)
tc.assertEqual(s.popSmallest(), 1)
tc.assertEqual(s.popSmallest(), 2)
tc.assertEqual(s.popSmallest(), 3)
s.addBack(1)
tc.assertEqual(s.popSmallest(), 1)
tc.assertEqual(s.popSmallest(), 4)
tc.assertEqual(s.popSmallest(), 5)

# Additional testcase
#
# Input
# ["SmallestInfiniteSet","popSmallest","popSmallest","addBack","popSmallest","addBack","popSmallest","popSmallest"]
# [[],[],[],[3],[],[2],[],[]]
#
# Expected
# [null,1,2,null,3,null,2,4]
s2 = SmallestInfiniteSet()
tc.assertEqual(s2.popSmallest(), 1)
tc.assertEqual(s2.popSmallest(), 2)
s2.addBack(3)
tc.assertEqual(s2.popSmallest(), 3)
s2.addBack(2)
tc.assertEqual(s2.popSmallest(), 2)
tc.assertEqual(s2.popSmallest(), 4)

