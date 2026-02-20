"""

Start: 4:12
End: TODO

https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10*(-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104

Questions
 - Data validation: nums will be longer than K
 - Do not neet to keep or return positions


Options
 - Option 1: Brute force. Sliding window, re-compute every time. Update max if max exceeded
   - T: O(n*k)
   - S: O(1)
 - Option 2: Sliding window. Compute average. As window moves, update only last and next
   - T: O(n)
   - S: O(1)
   - Pointers: Current left edge (or right edge). Math: ((Average * k) - nums[left] + nums[left + k]) / k
   - Optimization: k won't change. We can just keep track of the sum


"""
from typing import List
from unittest import TestCase


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_window_sum = 0
        current_window_sum = None
        left_index = 0

        for i in range(k):
            max_window_sum += nums[i]
        
        current_window_sum = max_window_sum
        while (left_index + k) <= len(nums) - 1:
            current_window_sum = current_window_sum - nums[left_index] + nums[left_index + k] 
            if current_window_sum > max_window_sum:
                max_window_sum = current_window_sum
            left_index += 1
        
        return max_window_sum / (k * 1.0)


tc = TestCase()
s = Solution()
# tc.findMaxAverage(type(s.findMaxAverage([1,8,6,2,5,4,8,3,7])), int)
# TODO Checks will likely require some numerical accuracy updates
tc.assertEqual(s.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4), 12.75000)
tc.assertEqual(s.findMaxAverage(nums = [5], k = 1), 5)
tc.assertEqual(s.findMaxAverage(nums = [0,4,0,3,2], k = 1), 4)
