"""

Start: 3:24
End:

https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75

We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Example 4:

Input: asteroids = [3,5,-6,2,-1,4]
Output: [-6,2,4]
Explanation: The asteroid -6 makes the asteroid 3 and 5 explode, and then continues going left. On the other side, the asteroid 2 makes the asteroid -1 explode and then continues going right, without reaching asteroid 4.

Constraints:

2 <= asteroids.length <= 10^4
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0

Questions / notes:

 - Empty array? Won't happen
 - Data Any specific ordering? Order provides relative positioning
 - What if there's a tie? Can't happen - can't be stationary, can't be in the same place


Options

 - Option 1: Brute force: Step through time sequences, check for crashes. Some sort of complex data structure
 - Option 2: Recursive?
 - Option 3: Stack. Keep adding until there's a sign change. On sign change handle destruction or non-destruction.
   - T: O(n)
   - S: O(n)
   - Can we do better: Probably not

Edge cases


Notes

 - Lots of small issues. New_sign was pulled incorrectly, using 0 instead of i
 - We need to go through the stack in reverse order, rather than forwards. Missed this the first time. Using reversed in wonky - this may actually reverse rather than just reading backwards


"""
from typing import List
from unittest import TestCase


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        stack_sign = 1 if asteroids[0] > 0 else -1

        for i in asteroids:
            new_sign = 1 if i > 0 else -1
            print(i, new_sign, stack, stack_sign)

            if new_sign == stack_sign:
                stack.append(i)
            # elif stack_sign == -1:
            #     stack.append(i)
            else:
                
                for stack_i in reversed(stack):
                    if stack_i < 0:
                        stack_sign = stack_sign * -1
                        break
                    if abs(i) > abs(stack_i):
                        # print(i, stack_i, '>')
                        stack.pop()
                    elif abs(i) == abs(stack_i):
                        # print(i, stack_i, '=')
                        stack.pop()
                        i = 0
                        break
                    else:
                        # i < stack_i
                        # print(i, stack_i, '<')
                        i = 0
                        break
                
                if i != 0:
                    stack.append(i)
        print(stack)
        return stack


# Tests
tc = TestCase()
s = Solution()

# tc.assertEqual(s.asteroidCollision([5, 10, -5]), [5, 10])
# tc.assertEqual(s.asteroidCollision([8, -8]), [])
# tc.assertEqual(s.asteroidCollision([10, 2, -5]), [10])
# tc.assertEqual(s.asteroidCollision([3, 5, -6, 2, -1, 4]), [-6, 2, 4])
tc.assertEqual(s.asteroidCollision([-2,-1,1,2]), [-2,-1,1,2])
