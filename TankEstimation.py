#!/usr/bin/python

import random
from MyStatistics import *


class Estimator:
    """An estimator that contains an estimation function and keeps track of the mean and variance of its results"""

    def __init__(self, function, name):
        self.function = function
        self.name = name
        self.statistics = StatisticsAccumulator()

    # Return the estimate while maintaining the statistics
    def get_estimate(self, samples):
        estimate = self.function(samples)
        self.statistics.update_statistics(estimate)
        return estimate

    def get_name(self):
        return self.name

    def get_mean(self):
        return self.statistics.get_mean()

    def get_stdev(self):
        return self.statistics.get_stdev()


# The four ways of estimating the number of tanks given a list of samples
def max_likelihood_estimate(samples):
    return max(samples)


def mean_matching_estimate(samples):
    return 2.0 * sum(samples)/float(len(samples)) - 1


def gaps_estimate(samples):
    return 1 + max(samples) + (max(samples) - len(samples)) / float(len(samples))


def min_variance_unbiased_estimate(samples):
    y = max(samples)
    n = len(samples)
    return (y**(n+1) - (y-1)**(n+1)) / (y**n - (y-1)**n)


def run(t, n, s, runs):
    random.seed(s)

    # Create the estimator wrappers
    estimators = [Estimator(max_likelihood_estimate, 'ml'), Estimator(mean_matching_estimate, 'mm'),
                  Estimator(gaps_estimate, 'gaps'), Estimator(min_variance_unbiased_estimate, 'mvue')]

    print "Estimates for N =", n
    for i in xrange(runs):

        # Generate the 4 samples randomly
        samples = []
        for j in xrange(4):
            samples.append(random.randint(1, n+1))

        # Determine the estimates for the samples
        for e in estimators:
            estimate = e.get_estimate(samples)
            # print "%5s : %7d" % (e.name, estimate)

    # Output the results
    for e in estimators:
        print "OUTPUT :%s: \t %15.3f %15.3f" % (e.get_name(), e.get_mean(), e.get_stdev())
