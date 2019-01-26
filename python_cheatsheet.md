### list
```python
l = list()                  # initialize a list, or []
l.append(val)               # append at the end.
l.extend([vals])            # append the list at the end.
l.remove(val)               # remove the first found val.
l.pop()                     # pop the last one
sorted(l)                   # return a sorted list. use l.sort() to sort in place.
l[::-1]                     # return a reversed list. l.reverse() is in place. reversed(l) returns an iterator
l[:]                        # returns a copy of the array
```
There are also `insert(index, val)`, `index(val)`, `count(val)`. Use a dict instead if you need these.
### queues
```python
from collections import deque   # deque stands for double end queue
q = deque()
q.append(val)               # append on the right, O(1)
q.appendleft(val)           # append on the left, O(1)
q.pop()                     # remove from the right
q.popleft()                 # remove from the left
q.rotate(num)               # rotate num nodes to the right, good for slicing
q.clear()                   # remove everything
```

### sets
```python
s = set()
s.add(val)                  # add val to set
s.remove(val)               # remove val from set, raise KeyError is not exist
s.discard(val)              # remove val from set if exists
s.pop()                     # pop an arbitrary val
s.clear()                   # clear the whole set
```

### dictionary
```python
d = dict()
del d[key]                  # remove key from dict
d.items()                   # returns a list of (k, v)
d.iteritems()               # returns an iterator of (k, v)
d.iterkeys()                # returns an iterator of keys. better than d.keys()
d.itervalues()              # returns an iterator of values. better than d.values()
from collections import defaultdict
defaultdict()               # can add without checking if key exists
```

### Counter
```python
from collections import Counter
c = Counter(list)           # create counter
c.most_common(num)          # returns the num most common key-val tuple
```

### heaps
```python
import heapq
l = []
heapq.heapify(l)            # to create a heap, convert a list by heapify.
heapq.heappush(l, val)      # push to heap, log(n)
heapq.heappop(l)            # pop from heap, log(n)
```

### functional programming
filter()
map()
reduce()
zip()

### list comprehension
```python
[f() for x in list]
```

### ternary condition
```python
1 if True else 2
```

### main
```python
if __name__ == "__main__":
    main()
```
