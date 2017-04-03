"""
Time and space efficient running median.

The container has space complexity O(N) where N is the number of elements. The
running median can be updated in O(log N) time.

Implementation notes

Running median uses two heaps internally, a min- and max-heap. Each new element
is pushed to one of these heaps after comparing against the root nodes. If the
heaps differ in length by more than one, then the larger heap is popped and the
value is pushed to the other heap. The median is either the root node of the
larger heap or the average of the root nodes of both heaps if they are the same
length.

http://stackoverflow.com/questions/10657503/find-running-median-from-a-stream-of-integers
"""
from collections.abc import Sequence
import heapq


class RunningMedian:
    """Running median of a stream of elements"""
    def __init__(self):
        self._min_heap = MinHeap()
        self._max_heap = MaxHeap()

    def push(self, x):
        if not len(self._max_heap):  # First entry
            self._max_heap.heappush(x)
        elif not len(self._min_heap):  # Second entry
            if x > self._max_heap[0]:
                self._min_heap.heappush(x)
            else:  # Move first entry from max- to min-heap; push second to max-
                self._min_heap.heappush(self._max_heap.heappop())
                self._max_heap.heappush(x)
        else:
            # Add next entry to one of the heaps
            if x < self._max_heap[0]:  # Add to max heap
                self._max_heap.heappush(x)
            else:
                self._min_heap.heappush(x)

            # Balance the size of the heaps
            if len(self._max_heap) > len(self._min_heap) + 1:
                self._min_heap.heappush(self._max_heap.heappop())
            elif len(self._min_heap) > len(self._max_heap) + 1:
                self._max_heap.heappush(self._min_heap.heappop())

    def median(self):
        if len(self._max_heap) is len(self._min_heap) + 1:
            return self._max_heap[0]
        elif len(self._min_heap) is len(self._max_heap) + 1:
            return self._min_heap[0]
        else:
            return (self._max_heap[0] + self._min_heap[0]) / 2


class MinHeap(Sequence):
    """Convenience object for heapq functions"""
    def __init__(self):
        self.h = []

    def heappush(self, x):
        heapq.heappush(self.h, x)

    def heappop(self):
        return heapq.heappop(self.h)

    def __getitem__(self, i):
        return self.h[i]

    def __len__(self):
        return len(self.h)


class MaxHeap(MinHeap):
    """Convenience object for heapq functions with comparisons reversed"""
    def heappush(self, x):
        heapq.heappush(self.h, MaxHeapObj(x))

    def heappop(self):
        return heapq.heappop(self.h).val

    def __getitem__(self, i):
        return self.h[i].val


class MaxHeapObj:
    """Convenience object that reverses the comparison functions"""
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)
