"""

Start: 11:27
End: 11:32

https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
 

Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100


Options
 - Option 1: Brute force. Keep current altitude and max altitude. Iterate through gains, update if current altitude exceeds max
   - T: O(n)
   - S: O(1)
   - Can we do better: Probably not. We need at least O(n) time, and space can't get lower. 

Edge cases

 - All 0: Fine, any 0

Notes

 - OK, no trick. This is pretty straight forward
 - Can use ternary statement or max(current, max_seen)


"""
from typing import List
from unittest import TestCase

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_seen = current_altitude

        for i in gain:
            current_altitude += i

            max_seen = max(current_altitude, max_seen)
        
        return max_seen

tc = TestCase()
s = Solution()

tc.assertEqual(s.largestAltitude(gain = [-5,1,5,0,-7]), 1)
tc.assertEqual(s.largestAltitude(gain = [-4,-3,-2,-1,4,3,2]), 0)
tc.assertEqual(s.largestAltitude(gain = [0,0,0,0]), 0)
