import heapq
from random import randint

print '====== heap with dict/tuples/lists elemet ======'
l = [{randint(1, 10): randint(1, 10)} for i in range(5)]
print 'random list of dicts/tuples/lists l: ', l
heapq.heapify(l)
print 'heapq.heapify(l) rearranges l, based on the key/first element of tuples: ', l
n = {randint(1, 10): randint(1, 10)}
heapq.heappush(l, n)
print 'heapq.heappush(l, n) a random integer n: ', n
print 'after heappush the list becomes: ', l
print 'heapq.heappop(l) returns: ', heapq.heappop(l)
print 'after heappop the list becomes: ', l
print 'heapq.nsmallest(3, l) returns smallest 3 elements in heap: ', heapq.nsmallest(3, l)


print '====== fixed length max heap ======'
class MaxFixedHeap():
    def __init__(self, size):
        self.heap = []
        self.size = size
        heapq.heapify(self.heap)

    def push(self, val):
        if len(self.heap) < self.size:
            heapq.heappush(self.heap, -1 * val)
        else:
            if val > self.heap[0] * -1:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, -1 * val)

    def pop(self):
        return -1 * heapq.heappop(self.heap)

    def __str__(self):
        return str([i * -1 for i in self.heap])

h = MaxFixedHeap(3)
h.push(1)
h.push(2)
h.push(3)
print 'pushed 1, 2, 3 into the heap: ', h

h.push(4)
print 'pushed 4 into the heap: ', h

h.push(-1)
print 'pushed -1 into the heap: ', h

print 'pop returns: ', h.pop()
