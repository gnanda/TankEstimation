#!/usr/bin/python

import matplotlib.pyplot as plt
import sys


def main():
    if not len(sys.argv) == 2:
        print "Usage: ./generate_plots.py estimator_name"
        exit(1)

    estimator_name = sys.argv[1]
    f = open("data/" + estimator_name + ".txt", 'r')

    x = []
    y = []
    e = []

    for line in f:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))
        e.append(1.96 * float(values[2]))

    f.close()

    plt.figure()
    plt.title(estimator_name)
    plt.xlabel('N')
    plt.ylabel('N_hat')
    plt.axis([1, 5000, 1, 7000])
    plt.plot(x, x, 'r-', label="Actual")
    plt.legend()
    plt.errorbar(x, y, yerr=e, fmt='ko')
    #plt.show()
    plt.savefig("figures/" + estimator_name + "_plot.png", format="png")


if __name__ == '__main__':
    main()