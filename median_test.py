import unittest

import heapq

from median import MaxHeapObj, MaxHeap, MinHeap


class MinHeapTest(unittest.TestCase):
    def test_min_heap(self):
        minh = MinHeap()
        # add some values
        fst_x = 12
        snd_x = 4
        minh.heappush(fst_x)
        minh.heappush(snd_x)
        # fetch "top" values
        self.assertEqual(minh[0], snd_x)  # "4 12"
        # fetch and remove "top" values
        self.assertEqual(minh.heappop(), snd_x)  # "4 12"


class MaxHeapTest(unittest.TestCase):
    def test_max_heap(self):
        maxh = MaxHeap()
        # add some values
        fst_x = 12
        snd_x = 4
        maxh.heappush(fst_x)
        maxh.heappush(snd_x)
        # fetch "top" values
        self.assertEqual(maxh[0], fst_x)  # "12 4"
        # fetch and remove "top" values
        self.assertEqual(maxh.heappop(), fst_x)  # "12 4"


class MaxHeapObjTest(unittest.TestCase):
    def test_push_pop(self):
        x = 42
        maxh = []
        heapq.heappush(maxh, MaxHeapObj(x))
        val = maxh[0].val  # fetch max value
        self.assertEqual(x, val)
        pop_val = heapq.heappop(maxh).val  # pop max value
        self.assertEqual(x, pop_val)
