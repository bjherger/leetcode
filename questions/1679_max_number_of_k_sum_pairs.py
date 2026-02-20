"""

Start: 3:58
End: 4:12

https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.
Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
 

Constraints:

1 <= nums.length <= 10**5
1 <= nums[i] <= 10**9
1 <= k <= 10**9

Questions
 - Empty array: Not an issue - at least 1. If 1 element, return 0 (no pair)
 - Assuming no data validation
 - Can't re-use items (they're removed)

Options
 - Option 1: Brute force. Try every possible pair, replace w/ None or otherwise remove when match found
   - T: O(n2)
   - S: O(1) (Modify array in place) or O(n) (can't modify in place)
 - Option 2: Sort, check pairs with pointer on each end
   - T: O(nlgn) (sort)
   - S: O(1) (Modify array in place) or O(n) (can't modify in place). Probably O(n)
   - Can we do better? Decreasing time to O(n) or space to O(1)?

"""
from typing import List
from unittest import TestCase


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_pairs = 0
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            pair_sum = nums[l] + nums[r]
            if pair_sum > k:
                r -= 1
            elif pair_sum < k:
                l += 1
            else:
                num_pairs += 1
                l += 1
                r -= 1
        return num_pairs


tc = TestCase()
s = Solution()
# tc.maxOperations(type(s.maxOperations([1,8,6,2,5,4,8,3,7])), int)
tc.assertEqual(s.maxOperations(nums = [1,2,3,4], k = 5), 2)
tc.assertEqual(s.maxOperations(nums = [3,1,3,4,3], k = 6), 1)
