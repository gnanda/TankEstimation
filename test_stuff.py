#!/usr/bin/python

import unittest
import math
import random
from TankEstimation import *
from MyStatistics import *

# Really crappy unit tests to check basic functionality

TOLERANCE = 0.001
def approx_equals(a, b):
    return math.fabs(a - b) < TOLERANCE


class EstimatorTestCase(unittest.TestCase):
    # Use the samples from the book to make sure the functions are defined correctly
    def runTest(self):
        samples = [952, 1923, 2000, 1927]
        assert int(max_likelihood_estimate(samples)) == 2000
        assert int(mean_matching_estimate(samples)) == 3400
        assert int(gaps_estimate(samples)) == 2500
        assert int(min_variance_unbiased_estimate(samples)) == 2499


class StatisticsAccumulatorTestCase(unittest.TestCase):
    def runTest(self):
        statistics = StatisticsAccumulator()

        # Use the numbers from 1 to 11
        samples = range(1, 12)
        # Shuffle them to ensure no systematic error
        random.shuffle(samples)

        # Add the samples one at a time
        for s in samples:
            statistics.update_statistics(s)

        assert approx_equals(statistics.get_mean(), 6.0)
        assert approx_equals(statistics.get_variance(), 10.0)
        assert approx_equals(statistics.get_stdev(), 3.1623)


if __name__ == '__main__':
    unittest.main()