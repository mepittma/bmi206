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
quick_rand = []
bubble_rand = []

quick_sorted = []
bubble_sorted = []

quick_rev = []
bubble_rev = []

# Test the time each function takes to run on lists from 100 to 1000 in
# increments of 100
for i in np.arange(100,1001,100):

    # Test on a randomly-chosen vector of integers
    vec = np.random.randint(0, 2000, i)
    quick_rand.append(time_sort(vec, "quick"))
    bubble_rand.append(time_sort(vec, "bubble"))

    # Test on a pre-sorted vector of integers
    vec = np.arange(0, i)
    quick_sorted.append(time_sort(vec, "quick"))
    bubble_sorted.append(time_sort(vec, "bubble"))

    # Test on a reverse-sorted vector of integers
    vec = list(reversed(range(i)))
    quick_rev.append(time_sort(vec, "quick"))
    bubble_rev.append(time_sort(vec, "bubble"))

# Make a graph showing time for the different types of input lists
create_fig(quick_rand, bubble_rand, "Random List Input")
create_fig(quick_sorted, bubble_sorted, "Sorted List Input")
create_fig(quick_rev, bubble_rev, "Reverse-Sorted Input")