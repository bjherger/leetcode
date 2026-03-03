"""

Start: 1:33
End: 2:03

https://leetcode.com/problems/dota2-senate/description/?envType=study-plan-v2&envId=leetcode-75

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

 - Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
 - Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

Example 1:

Input: senate = "RD"
Output: "Radiant"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And in round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:

Input: senate = "RDD"
Output: "Dire"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And the third senator comes from Dire and he can ban the first senator's right in round 1.
And in round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

Constraints:

n == senate.length
1 <= n <= 10^4
senate[i] is either 'R' or 'D'.

Questions / notes:

 - Why so much flavor text?
 - Strategy is likely to ban a member from the opposing party. 
 - Does it matter whether it is an early or later one? Earlier means that they do not get to excercise their right to ban, whereas later simply skips them. So banning the earliest opposition is probably the best
 - Are these in the round? No, each round has a clear start and end
 - For announcing victory: Is it all senators, or just senators remaining in this round? It appears to be all senators

Options

 - Option 1: Brute force. For each senator, iterate through all senators. Block any opposing senators, or if none remain delcare victory
  - T: O(n2)
  - S: O(n) (array of blocked) (or O(1) if modify in place)
 - Option 2: Two pointers. Pointers for leading R and leading D, counter for remaining R and D. First pass: populate counters. While no victory, sweep through array negating. Wrap around logic so last senator would ban earliest opposing senator
   - T: O(n2)
   - S: O(n) (array of blocked) or O(1) if modify in place
 - Option 3: Two queues. First pass add to queues. Second pass: While both queues contain elements, choose queue w/ earlier head, remove head of other queue
   - T: O(n)
   - S: O(n) (queues)


Notes for next time:
 - Missed that option 2 is actually n2
   - Have to actually advance pointer to next member of the same party
 - Using queue structure
 - Need to remember name of collections.Deque
 - Original did a simple check that allowed the 0th to vote an unlimited number of times. This isn't quite right. After someone votes, we need to append them to the end of their team's queue. Adding an index to keep track of who's turn it is
 - I tried at first to do a for loop, but this is messy manually incrementing the index and wrapping around w/ %= len(senate) is much cleaner
 - This was cleaner than other questions, but still not flawless. 
"""
from unittest import TestCase

from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = deque()
        r = deque()
        index = 0 

        for i, e in enumerate(senate):
            if e == 'D':
                d.append(i)
            else:
                r.append(i)

        while len(d) >0 and len(r) > 0:
            # print(d, r)
        
            if d[0] == index:
                r.popleft()
                d.append(d.popleft())
            elif r[0] == index:
                d.popleft()
                r.append(r.popleft())
            index += 1
            index %= len(senate)
        # print(d, r)
        return 'Radiant' if len(d) == 0 else 'Dire'
    


# Tests
tc = TestCase()
s = Solution()
tc.assertEqual(s.predictPartyVictory("RD"), "Radiant")
tc.assertEqual(s.predictPartyVictory("RDD"), "Dire")
