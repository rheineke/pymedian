import unittest

from integral_median import RunningMedian


class RunningMedianTest(unittest.TestCase):
    @unittest.skip
    def test_example_one(self):
        xs = [5, 60, 35, 42, 2, 38, 6, 5, 8, 300, 1500, 900, 4, 400, 2]
        expected_medians = [
            5, 32.5, 35, 38.5, 35, 36.5, 35, 20.5, 8, 21.5, 35, 36.5, 35, 36.5,
            35
        ]
        id_func = lambda x: x
        mc = RunningMedian(key_function=id_func, inverse_key_function=id_func)
        for x, expected_median in zip(xs, expected_medians):
            mc.push(x)
            median = mc.median()
            print(median)
            self.assertEqual(median, expected_median)

    def test_example_two(self):
        xs = [1, 5, 4, 1, 3, 2, 4]
        expected_median = [
            1, 3, 4, 2.5, 3, 2.5, 3
        ]

        id_func = lambda x: x
        mc = RunningMedian(key_function=id_func, inverse_key_function=id_func)
        for x in xs:
            mc.push(x)
            print('Median value: {}\n'.format(mc.median()))
