"""
Questions
 - Asymmetric follows: Yes
 - Snapshot format: Choose data structure
 - is following should accept int
 - Snapshots could hold deltas or entirely separate. 
 - Ordering doesn't matter for get_followees or get_followers

Plan
 - array of snapshots, with index as snapshot id
 - Snapshot contains hashmap from user to a set of all the folks they follow

Plan stage 2
 - Option 1: Existing data structure. Get followees is O(1), get followers O(n)
 - Option 2: Additional followers data structure. 2x. O(1) and O(1), concerns on keeping in sync, extra storage space

Plan stage 3

 - List of folks followed by user_id, get list of folks followed
"""

import copy

class SocialNetwork:
    def __init__(self):
        self.snapshots = list()
        self.snapshots.append(dict())

    def follow(self, user_a: int, user_b: int) -> None:
        if user_a == user_b:
            return None
        
        # A->B
        user_obj = self.get_latest_user_object(user_a)
        following = user_obj.get('following', set())
        following.add(user_b)
        user_obj['following'] = following
        
        self.get_latest_snapshot()[user_a] = user_obj

        # B-> A
        user_obj = self.get_latest_user_object(user_b)
        followers = user_obj.get('followers', set())
        user_obj['followers'] = followers
        followers.add(user_a)
        self.get_latest_snapshot()[user_b] = user_obj

    def unfollow(self, user_a: int, user_b: int) -> None:  
        # A->B
        previous_follows = self.get_latest_user_object(user_a).get('following', set())
        if user_b in previous_follows:
            previous_follows.remove(user_b)

        # B->A
        previous_followers = self.get_latest_user_object(user_b).get('followers', set())
        if user_a in previous_followers:
            previous_followers.remove(user_a)

    
    def get_latest_snapshot(self):
        return self.snapshots[-1]

    def get_latest_user_object(self, user):
        return self.get_latest_snapshot().get(user, dict())

    def snapshot(self) -> int:
        self.snapshots.append(copy.deepcopy(self.snapshots[-1]))
        return len(self.snapshots) - 2
  

    def is_following(self, user_a: int, user_b: int, snapshot_id: int) -> bool:
        return user_b in self.snapshots[snapshot_id].get(user_a, dict()).get('following', set())

    def recommend(self, user_id: int, snapshot_id: int, k: int = 5):
        snapshot = self.snapshots[snapshot_id]
        user_following = snapshot.get(user_id, dict()).get('following', set())

        second_dict = dict()

        for i in user_following:
            for j in snapshot.get(i, dict()).get('following', set()):
                if j!= user_id and j not in user_following:
                    second_dict[j] = second_dict.get(j, 0) + 1

        sorted(second_dict.keys(), key= second_dict.values(), ascending=False)[:k]

network = SocialNetwork()
network.follow(1, 2)

snap0 = network.snapshot()  # snap0 = 0
network.unfollow(1, 2)
snap1 = network.snapshot()  # snap1 = 1

print(network.snapshots[0])
print(network.snapshots[1])


assert network.is_following(1, 2, snap0) == True
assert network.is_following(1, 2, snap1) == False

# Follow
assert network.is_following(3, 2, snap0) == False

# Unfollow

# 