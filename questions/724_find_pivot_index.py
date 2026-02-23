"""

Start: 11:37
End: 11:48

https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0


Questions:
 - Is pivot in sums? No, strictlly left and strictly right

Options
 - Option 1: Brute force. Loop 1 compute sum. Loop 2 keep track of left sum and right sum
   - T: O(n)
   - S: O(1)
   - Can we do better: Maybe get it down to a single loop. Maybe some optimizations around starting in middle, though this could void left most requirement

Edge cases

 - No pivot
 - Multiple pivots: Return left most
 - Pivot is index 0 (left sum is 0, right sum is also 0)

Notes

 - No special tricks. It's just straight forward
 - Lots of small details (e.g. return left most index, whether pivot index is included in sums)
 - Most of the time was reading, setting up tests.


"""
from typing import List
from unittest import TestCase

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = 0
        left_sum = right_sum

        for n in nums:
            right_sum += n
        
        for (i,n) in enumerate(nums):
            if left_sum == (right_sum - n):
                return i
            
            left_sum += n
            right_sum -= n
        
        return -1

tc = TestCase()
s = Solution()

tc.assertEqual(
    s.pivotIndex(
        nums = [1,7,3,6,5,6])
    , 3
    )


tc.assertEqual(
    s.pivotIndex(
        nums = [1,2,3]
    )
    , -1
    )

tc.assertEqual(
    s.pivotIndex(
        nums = [2,1,-1]
    )
    , 0
    )