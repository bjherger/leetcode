"""

Start: 12:22
End: 12:37

https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75

You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example 1:

Input
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
Output
[null, 1, 2, 3, 3]

Explanation
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1], range is [-2999,1], return 1
recentCounter.ping(100);   // requests = [1, 100], range is [-2900,100], return 2
recentCounter.ping(3001);  // requests = [1, 100, 3001], range is [1,3001], return 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002], range is [2,3002], return 3

Constraints:

1 <= t <= 109
Each test case will call ping with strictly increasing values of t.
At most 104 calls will be made to ping.

Questions / notes:

 - Strictly increasing? Yes
 - Ties? No, strictly larger
 - Inclusive of incoming? Yes

 n = number of pings
 m = length of window (ie 3000)

Options
 - Option 1: Brute force: Create an set. On addition iterate through all elements
   - T: O(n)
   - S: O(n)
 - Option 2: Array, left pointer at latest valid, right pointer at end
   - T: O(1)
   - S: O(m) = constant
 - Option 3: Linked List (no native implementation in python), option 4: Array, but remove rather than left pointer. Unclear if this is any more efficient
  - Option 4: collections.deque

Notes for next time:

 - collections.dequeue is mostly the key. Knowing methods is super helpful
   - q[0] for peaking
   - q.append() for adding
   - q.pop() for removing

"""
from unittest import TestCase
from collections import deque


class RecentCounter:
    def __init__(self, delta = 3000):
        self.pings = deque()
        self.delta = delta
        

    def ping(self, t: int) -> int:
        self.pings.append(t)
        while self.pings[0] < t - self.delta:
            self.pings.popleft()
        return len(self.pings)


# Tests
tc = TestCase()
counter = RecentCounter()

tc.assertEqual(counter.ping(1), 1)
tc.assertEqual(counter.ping(100), 2)
tc.assertEqual(counter.ping(3001), 3)
tc.assertEqual(counter.ping(3002), 3)
