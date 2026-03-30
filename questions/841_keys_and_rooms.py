"""
Start: 15:06
End: 15:14

https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75

There are `n` rooms labeled from `0` to `n - 1` and all the rooms are locked except for room `0`.
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks,
and you can take all of them with you to unlock the other rooms.

Given an array `rooms` where `rooms[i]` is the set of keys that you can obtain if you visited room `i`, return `true` if you can
visit all the rooms, or `false` otherwise.

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: We visit room 0 and pick up key 1.
Then we visit room 1 and pick up key 2.
Then we visit room 2 and pick up key 3.
Then we visit room 3.
Since we were able to visit every room, we return true.

Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room 2 since the only key that unlocks room 2 is in that room.

Constraints:

- n == rooms.length
- 2 <= n <= 1000
- 0 <= rooms[i].length <= 1000
- 1 <= sum(rooms[i].length) <= 3000
- 0 <= rooms[i][j] < n
- All the values of rooms[i] are unique.

Questions / notes:
 - At least 0th room: Yes

Options
 - Breadth first search. For current room, add rooms w/ keys found but not yet searched to queue
  - How to store keys? Set or array indexed by room. Store as set, can get set size to check completion 

Notes for next time:
"""
from collections import deque
from unittest import TestCase
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        d = deque()
        d.append(0)
        seen = set()
        seen.add(0)

        while len(d) > 0:
            c = d.popleft()

            for k in rooms[c]:
                if k not in seen:
                    d.append(k)
                    seen.add(k)
        return len(seen) == len(rooms)


tc = TestCase()
tc.assertEqual(Solution().canVisitAllRooms([[1], [2], [3], []]), True)
tc.assertEqual(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]), False)

