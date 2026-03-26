"""

Start: 16:06
End: 17:00
Interview-style (no LeetCode URL). Inspired by system design / OOP exercises.

Implement a **SocialNetwork** that supports asymmetric follow relationships, **point-in-time snapshots**, and **recommendations** based on overlap with followees’ follow lists.

**Follow model**

- `follow(user_a, user_b)` means *user_a follows user_b* (directed edge A → B).
- If `user_a == user_b`, do nothing.
- You may store redundant structures (e.g. both “following” and “followers”) for query efficiency; ordering of sets does not matter unless a method specifies a sort order.

**Snapshots**

- The network evolves through `follow` and `unfollow`.
- `snapshot() -> int` records the **current** graph as an immutable view and returns its integer `snapshot_id`. After the call, further mutations must not change data queried by that id. (Any internal representation is fine as long as behavior matches.)
- `snapshot_id` values are stable integers usable with `is_following` and `recommend`.
- The initial empty network exists before the first `snapshot()`; the first `snapshot()` returns `0` when defined as in the examples below.

**Queries**

- `is_following(user_a, user_b, snapshot_id) -> bool`: at the given snapshot, does `user_a` follow `user_b`?
- `list_followers(user_id, snapshot_id) -> list[int]`: at the given snapshot, return the user ids **who follow** `user_id` (incoming edges). Each id appears at most once. **Order is unspecified** (tests compare as sets).
- `recommend(user_id, snapshot_id, k=5) -> list[int]`: consider users **not** equal to `user_id` and **not** already followed by `user_id` at that snapshot. For each candidate `j`, let the **score** be the number of distinct users `u` such that `user_id` follows `u` at that snapshot and `u` follows `j` at that snapshot. Return up to `k` candidates with **highest score** first; break ties by **smaller user id** first.

**Example 1 (snapshots + is_following)**

```
network = SocialNetwork()
network.follow(1, 2)
snap0 = network.snapshot()   # 0: 1 follows 2
network.unfollow(1, 2)
snap1 = network.snapshot()   # 1: 1 does not follow 2
```

Then `is_following(1, 2, snap0)` is True and `is_following(1, 2, snap1)` is False. The set of followers of `2` at `snap0` is `{1}`; at `snap1` it is empty.

**Example 2 (recommend)**

At a snapshot where: 1 follows 2 and 3; 2 follows 4; 3 follows 4; and no other edges matter for scores of 4, 5, 6:

- Candidate 4 has score 2 (via 2 and 3). Candidates 5 and 6 have score 0 unless other edges exist.

So `recommend(1, that_snapshot_id, k=1)` should return `[4]`.

Constraints (for this exercise):

- User ids are integers.
- `0 <= k <= 5000`.
- `snapshot_id` passed to queries always refers to a snapshot that was returned by a prior `snapshot()` on the same instance (or as specified in tests).

Questions / notes:

 - Recommendation: What to do w/ ties? Return lowest ID

Options

 - Snapshot changes: Deltas, or store entire network for each snapshot. Depending on frequency of snapshot, deltas may be more storage efficient, but add compute to run actions on a specific snapshot (or any snapshot after s0)
 - Objects: has maps or user class
   - user class more scalalbe, easier to read
   - snapshot class: could allow for future extensibility, no clear upside at this stage. Can be added / converted later
   - Store snapshots as array, with array index as snapshot ID
   - Store snapshot as hasmap / set of users.
   - Recommend: Counter, return top k most common items
   - List followers: Could either itererate through all other users (compute expensive), keep overlapping records of following / followers (requires atomic transactions, storage expensive), or switch to a matrix (storage expensive, particularly for sparse matrix), or use a sparse matrix (logically complex, may need specialized data structure to support following / follower lookups)



Notes for next time:

 - Need to be more familiar w/ the ins and outs of collections.Counter(), sorted keys
 - Recommendation: can sort by ID either at the same time as counts, or after
 - Using a class is a lot cleaner than all of the random hashmaps. 

"""
from __future__ import annotations

from unittest import TestCase

import copy
import pprint

from collections import Counter

class User:
    
    def __init__(self, id) -> None:
        self.following = set()
        self.followers = set()
        self.id = id

    def __repr__(self) -> str:
        return f"  id: {self.id}, \n   following: {self.following}, \n   followers: {self.followers}"

class SocialNetwork:
    def __init__(self) -> None:
        self.snapshots = list()
        self.snapshots.append(dict())
        

    def follow(self, user_a: int, user_b: int) -> None:
        if user_a == user_b:
            return None
        
        s = self.snapshots[-1]
        if user_a not in s.keys():
            s[user_a] = User(user_a)
        
        if user_b not in s.keys():
            s[user_b] = User(user_b)

        s[user_a].following.add(user_b)
        s[user_b].followers.add(user_a)


    def unfollow(self, user_a: int, user_b: int) -> None:
        # No self follows enforced on follow()

        s = self.snapshots[-1]

        if user_a in s.keys() and user_b in s[user_a].following:
            s[user_a].following.remove(user_b)

        if user_b in s.keys() and user_a in s[user_b].followers:
            s[user_b].followers.remove(user_a)

    def snapshot(self) -> int:
        self.snapshots.append(copy.deepcopy(self.snapshots[-1]))
        return len(self.snapshots) - 2

    def is_following(self, user_a: int, user_b: int, snapshot_id: int) -> bool:
        if (snapshot_id < len(self.snapshots)
            and user_a in self.snapshots[snapshot_id]
            and user_b in self.snapshots[snapshot_id][user_a].following):
            return True
        return False

    def list_followers(self, user_id: int, snapshot_id: int) -> list[int]:
         if (snapshot_id < len(self.snapshots)
            and user_id in self.snapshots[snapshot_id]):
            return self.snapshots[snapshot_id][user_id].followers

    def recommend(self, user_id: int, snapshot_id: int, k: int = 5) -> list[int]:

        recommendations_dict = Counter()
        empty_user = User(None)

        if (snapshot_id < len(self.snapshots)
            and user_id in self.snapshots[snapshot_id]):
            following = self.snapshots[snapshot_id][user_id].following
            for i in following:

                for j in self.snapshots[snapshot_id].get(i, empty_user).following:

                    if j != user_id and j not in following:
                        recommendations_dict[j] += 1

        top_k = sorted(recommendations_dict.items(), key=lambda x: (-x[1], x[0]))[:k]
        return list(map(lambda x: x[0], top_k))



    def print_latest_snapshot(self):
        pprint.pprint(self.snapshots[-1])

    def print_specific_snapshot(self, snapshot_id):
        pprint.pprint(self.snapshots[snapshot_id])


tc = TestCase()
network = SocialNetwork()
network.follow(1, 2)
# network.print_latest_snapshot()
snap0 = network.snapshot()
# network.print_specific_snapshot(0)
network.unfollow(1, 2)
snap1 = network.snapshot()

tc.assertEqual(network.is_following(1, 2, snap0), True)
tc.assertEqual(network.is_following(1, 2, snap1), False)
tc.assertEqual(network.is_following(3, 2, snap0), False)
tc.assertEqual(set(network.list_followers(2, snap0)), {1})
tc.assertEqual(set(network.list_followers(2, snap1)), set())

# Recommend: build state, freeze, then query
rec_net = SocialNetwork()
rec_net.follow(1, 2)
rec_net.follow(1, 3)
rec_net.follow(2, 4)
rec_net.follow(3, 4)
snap_rec = rec_net.snapshot()
tc.assertEqual(rec_net.recommend(1, snap_rec, k=1), [4])
