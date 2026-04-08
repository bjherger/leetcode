
"""
You are building an in-memory, single-threaded analytics service for ChatGPT chat sessions. It ingests a real-time, globally non-decreasing stream of interaction logs and answers “recent count” queries efficiently.

Suppose each log records an interaction:

user_id: str
chat_id: int (unique per user)
timestamp: int (in minutes)
We frequently need the number of interactions for a given (userid, chatid) that occurred in the last 15 minutes, defined as the closed interval [T-14, T], where T is the largest timestamp seen so far in the entire stream.

Implement:

process_event(user_id: str, chat_id: int, timestamp: int)
get_num_recent_interactions(user_id: str, chat_id: int) -> int
Assumptions and Requirements:

events are non-decreasing in timestamp, and no duplicates.
log and query volumes are high, so we want both operations to be efficient.
Bounded memory (active-window only): You have enough memory for state proportional to the number of chats/events in the last 15 minutes, but not proportional to total historical events or total chats ever seen.
The start code contains a basic test as a simple example.

Suppose each event has an additional field:

event_type: str
There are two event types:

interact: user sends a message and receives a response in a chat
end: user explicitly ends a chat session. End events may arrive after arbitrary duration or never.
As we process the real time logs, we want to know the current number of active sessions for a user.

A session is active if it has an interact event within the past 15 minutes, and has not received an end event after the latest interact event.

Modify processevent() and support getactivesessioncount():

process_event(user_id: str, chat_id: int, timestamp: int, event_type: str = "interact")
get_active_session_count(user_id: str) -> int
For example:

print(tr.get_active_session_count("u1"))      # 0


Invariants
 - Number of interactions for a given userid, chat_id in past 15 minutes, including boundaries
 - Time is max timestamp currently seen
 - Timestamp in minutes

Options
 - Data structure
   - hashmap from user_id to DLL of chat timestamp and chat ID 
   - Process event: Would write to the front of the double linked list 
     - optionally remove from end
     - Update latest TS
   - get_num_recent_interactions would remove from end, and return length

Future improvements
 - hashmap key to user and chat_id as, or nested hashmaps. In this case, __expire_sessions__ would still remove from the left, and len(d) would be constant timestamp

{
(user_id, chat_id): deque()
}

{
(user_id,): chat_id: deque()
}
"""

from collections import deque

WINDOW = 15  # minutes

class Event:
    def __init__(self, chat_id: int, timestamp: int, event_type):
        self.chat_id = chat_id
        self.ts = timestamp
        self.type = event_type

    def __repr__(self):
        return f"[chat_id={self.chat_id}, ts={self.ts}, type={self.type}]"


class SessionTracker:
    def __init__(self) -> None:
        self.latest_ts = -1
        self.sessions = {}

    def process_event(self, user_id: str, chat_id: int, timestamp: int, event_type="interact") -> None:
        self.latest_ts = max(timestamp, self.latest_ts)
        
        d = self.sessions.get(user_id, deque())

        d.appendleft(Event(chat_id, timestamp, event_type))
        self.__expire_sessions__(d, self.latest_ts)
        self.sessions[user_id] = d

    def get_num_recent_interactions(self, user_id: str, chat_id: int) -> int:
        
        d = self.sessions.get(user_id, deque())
        self.__expire_sessions__(d, self.latest_ts)
        
        self.sessions[user_id] = d

        count = 0

        for e in d:
            if e.chat_id == chat_id:
                count += 1
        
        return count

    def get_active_session_count(self, user_id: str) -> int:
        d = self.sessions.get(user_id, deque())
        active_sessions = set()
        self.__expire_sessions__(d, self.latest_ts)
        
        self.sessions[user_id] = d

        for e in reversed(d):
            if e.type == "end" and e.chat_id in active_sessions:
                active_sessions.discard(e.chat_id)

            else:
                active_sessions.add(e.chat_id)

        return len(active_sessions)
    
    def __expire_sessions__(self, d, latest_ts):
        expiration_ts = latest_ts - WINDOW

        if len(d) < 1:
            return d

        cursor = d[-1]

        while cursor.ts < expiration_ts:
            d.pop()
            cursor = d[-1]



tr = SessionTracker()

# t = 0-10  ── three interactions across two chats
tr.process_event("u1", 1, 0)  # chat 1 – first interact
tr.process_event("u1", 1, 5)  # chat 1 – second interact
tr.process_event("u1", 2, 10)  # chat 2 – first interact

assert tr.get_num_recent_interactions("u1", 1) == 2
assert tr.get_num_recent_interactions("u1", 2) == 1

# suppose u1 stopped interacting and we have processed events many from other users
tr.process_event("other", 99, 24)  # t = 24

assert tr.get_num_recent_interactions("u1", 1) == 0  # (chat 1 window expired)
assert tr.get_num_recent_interactions("u1", 2) == 1  # (chat 2 window not yet expired)

tr = SessionTracker()

tr.process_event("u1", 1, 0, "interact")
print(tr.get_active_session_count("u1"))      # 1

tr.process_event("u1", 1, 5, "end")
print(tr.sessions)
print(tr.get_active_session_count("u1"))      # 0

# TODO Test for 15 minute edge case

