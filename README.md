# Leetcode

Working through [Leetcode 75](https://leetcode.com/studyplan/leetcode-75/)

# Helpful python common lib classes

- **[deque](https://docs.python.org/3/library/collections.html#collections.deque)**: Doubly linked list of fixed-size blocks, in `collections`, O(1) append/pop from both ends, ideal for BFS queues and sliding windows. Common methods include `q.append()`, `q.appendleft()`, `q.pop()`, `q.popleft()`, `q[0]` to peek.
- **[defaultdict](https://docs.python.org/3/library/collections.html#collections.defaultdict)**: Dictionary with automatic default value initialization, in `collections`, avoids key errors when grouping or counting. Common usage includes `defaultdict(int)`, `defaultdict(list)`.
- **[Counter](https://docs.python.org/3/library/collections.html#collections.Counter)**: Hash map for frequency counting, in `collections`, O(1) average updates, useful for counting and top-k problems. Common methods include `c.update()`, `c.most_common(k)`.
- **[heapq](https://docs.python.org/3/library/heapq.html)**: Binary min-heap implemented over a list, in `heapq`, O(log n) push/pop, used for priority queues and top-k problems. Common methods include `heappush(h, x)`, `heappop(h)`, `heapify(list)`.
- **[bisect](https://docs.python.org/3/library/bisect.html)**: Binary search utilities for sorted lists, in `bisect`, O(log n) search and O(n) insert, useful for maintaining sorted order. Common methods include `bisect_left()`, `bisect_right()`, `insort()`.
- **[frozenset](https://docs.python.org/3/library/stdtypes.html#frozenset)**: Immutable set, built-in, hashable and usable as dict keys, O(1) membership checks. Created via `frozenset(iterable)`.
- **[dataclass](https://docs.python.org/3/library/dataclasses.html)**: Structured class generator, in `dataclasses`, auto-generates `__init__` and `__repr__`, useful for clean model objects. Declared with `@dataclass`.
- **[namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)**: Lightweight immutable tuple subclass with named fields, in `collections`, memory-efficient alternative to small classes. Created via `namedtuple("Name", ["field1", "field2"])`.
- **[lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)**: Memoization decorator, in `functools`, caches function calls for DP/DFS problems. Used as `@lru_cache(maxsize=None)`.
- **[Queue](https://docs.python.org/3/library/queue.html#queue.Queue)**: Thread-safe FIFO queue, in `queue`, safe for multithreading. Common methods include `put()`, `get()`.
- **[PriorityQueue](https://docs.python.org/3/library/queue.html#queue.PriorityQueue)**: Thread-safe priority queue, in `queue`, internally heap-based, useful in concurrent systems. Common methods include `put()`, `get()`.

