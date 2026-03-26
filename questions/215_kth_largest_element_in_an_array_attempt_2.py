"""
Start: 11:39
End: TODO

https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

Questions / notes:
 - Ties? Treat sequentially, doesn't matter which index is returned (or if stable)
 - K often less than N? Yes

Options

 - O1: Brute force - sort
 - O2: Min heap, constricted to size k
 - O3: Sorted array of size K, keep track of smallest element

 Implementing 2. What does this look like?
  - Represent the heap as an array, with childen and 2n+1 and 2n+2
  - Size of array is k
  - If array size <k, just add
  - If array size >=k, only add if current number is greater than index 0 (min)
  - Return index 0

Notes for next time:
 - Important to know minheap (`import heapq`, headpop, h[0] to peak)
"""

from unittest import TestCase
import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = list()
        for i in nums:
            if len(h) < k:
                heapq.heappush(h, i)
            elif i > h[0]:
                    heapq.heappushpop(h, i)
            print(i, h)
        
        return h[0]
        


tc = TestCase()
tc.assertEqual(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
tc.assertEqual(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)
