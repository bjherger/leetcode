"""

Start: 3:21
End: 3:46

https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
 

Constraints:

n == height.length
2 <= n <= 10**5
0 <= height[i] <= 10**4

Questions
 - Units: Don't matter. Assuming X units and Y units are the same
 - Empty list: Will return 0
 - Heights: Can be zero. If all zero, will return zero
 - Ties: Don't matter
 - Do I need to return the indices of the boundaries? No

Options
 - Option 1: Brute force. Create all possible fence post pairs
   - T: O(n^2)
   - S: O(1)
   - Can we do better? Maybe if we did some kind of sorting
   - We could optimize to break early by checking right posts in decending order or height, but this doesn't really change the worse case time
 - Option 2: Two pointers. One left, the other right. Move the lower line inward
"""
from typing import List
from unittest import TestCase


class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l_index = 0
        r_index = len(height) - 1
        max_area = 0

        while l_index < r_index:

            current_height = min(height[l_index],  height[r_index]) * (r_index - l_index)
            if current_height > max_area:
                max_area = current_height
            
            if height[l_index] < height[r_index]:
                l_index += 1
            else:
                r_index -=1

        return max_area


tc = TestCase()
s = Solution()
# tc.assertEqual(type(s.maxArea([1,8,6,2,5,4,8,3,7])), int)
tc.assertEqual(s.maxArea([1,8,6,2,5,4,8,3,7]), 49)
tc.assertEqual(s.maxArea([1,1]), 1)
