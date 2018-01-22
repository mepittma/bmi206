#!/usr/bin/env python3

import numpy as np
from sort import algs
import matplotlib.pyplot as plt
import time

# This script shows that the average time complexity for quicksort is O(n log n)
# while bubblesort has time complexity O(n^2).

def time_sort(vec, method):
    """
    This function takes a vector and sorting method as its input and outputs
    the time it took to run the functions (in seconds).
    """

    start = time.time()

    if method == "quick":
        algs.quicksort(vec)
    elif method == "bubble":
        algs.bubblesort(vec)

    return time.time() - start

def create_fig(quick, bubble, title):
    """
    This function is a very specific figure-generating function for the case in
    which a list composed of  # elements ranging from [100, 200, 300, ... , 1000]
    has been sorted with both quicksort and bubblesort. Input are the vectors
    containing the number of seconds taken to sort each list for both quickSort
    and bubblesort. A graph is saved for cases of random lists, sorted lists,
    and reverse-sorted lists.
    """
    x = np.arange(100, 1001, 100)

    plt.plot(x, quick, label='QuickSort')
    plt.plot(x, bubble, label='BubbleSort')

    plt.xlabel('N elements in list')
    plt.ylabel('Time to sort (seconds)')

    plt.title(title)
    plt.legend()
    plt.savefig('output/{}.png'.format(title), bbox_inches='tight')

    plt.clf()

# Create vectors to compare runtime
quick_avg = []
bubble_avg = []

# Test the time each function takes to run on lists from 100 to 1000 in
# increments of 100
for i in np.arange(100,1001,100):

    # Average the results from 100 trials
    quick_trials = []
    bubble_trials = []

    for j in range(0, 100):

        # Test on a randomly-chosen vector of integers
        vec = np.random.randint(0, 2000, i)
        quick_trials.append(time_sort(vec, "quick"))
        bubble_trials.append(time_sort(vec, "bubble"))

    # Average the contents of the trials together, append to times
    quick_avg.append(sum(quick_trials)/len(quick_trials))
    bubble_avg.append(sum(bubble_trials)/len(bubble_trials))


# Make a graph showing time for the different types of input lists
create_fig(quick_avg, bubble_avg, "Random List Input (avg over 100 trials)")

# Create a plot to demonstrate what n^2 and nlog(n) look like
x = np.arange(100, 1001, 100)

plt.plot(x, x * np.log2(x), label='nlog(n)')
plt.plot(x, x ** 2, label='n-squared')

plt.title("Reference functions")
plt.legend()
plt.savefig('output/reference.png', bbox_inches='tight')

plt.clf()
