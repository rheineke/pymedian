from array import array


class RunningMedian:
    def __init__(self, key_function, inverse_key_function):
        self.key = key_function
        self.inverse_key = inverse_key_function
        self.inputs = []  # Length n where n is number of elements
        self.key_counts = array("I")  # Length k where k is max key value
        self.total = 0
        # self.start_indices = []  # Length k where k is max key value

    def push(self, x):
        """Update interval storage. Time complexity O(1)"""
        self.inputs.append(x)
        # print('Inputs: {}'.format(self.inputs))

        # calculate the histogram of key frequencies:
        k = self.key(x)
        # print('Key value: {}'.format(k))
        if k >= len(self.key_counts):
            ext = [0] * (k - len(self.key_counts) + 1)
            self.key_counts.extend(ext)
        self.key_counts[k] += 1
        print(f"Key counts: {self.key_counts}\n")

        self.total += 1

    def median(self):
        """Calculate median and return. Time complexity O(k)"""
        # Calculate median index
        median_index = self.total // 2
        print(f"Median index: {median_index}")

        # Calculate the key value of the median index O(k)
        cumsum = 0
        i = 0
        for i, key_cnt in enumerate(self.key_counts):
            if cumsum + key_cnt >= median_index:
                break
            cumsum += key_cnt

        print(f"Key count index: {i}")
        # i = key(median value)
        # Cases:
        # 1. Number of elements even and cumsum == median_index
        # 2. Number of elements even and cumsum > median_index
        # 3. Number of elements odd
        input_median_index = self.inverse_key(i)
        # print('Input median index: {}'.format(input_median_index))
        return self.inputs[input_median_index]
        # if self.total % 2 == 0:
        # else:
        #


# def counting_sort():
#     # variables:
#     #    input -- the array of items to be sorted; key(x) returns the key for item x
#     #    n -- the length of the input
#     #    k -- a number such that all keys are in the range 0..k-1
#     #    count -- an array of numbers, with indexes 0..k-1, initially all zero
#     #    output -- an array of items, with indexes 0..n-1
#     #    x -- an individual input item, used within the algorithm
#     #    total, oldCount, i -- numbers used within the algorithm
#
#     # calculate the histogram of key frequencies:
#     for x in input:
#         count[key(x)] += 1
#
#     # calculate the starting index for each key:
#     total = 0
#     for i in range(k):  # i = 0, 1, ... k-1
#         oldCount = count[i]
#         count[i] = total
#         total += oldCount
#
#     # copy to output array, preserving order of inputs with equal keys:
#     for x in input:
#         output[count[key(x)]] = x
#         count[key(x)] += 1
#
#     return output
