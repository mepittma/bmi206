#!/usr/bin/env python3

import numpy as np
from sort import cond_algs as algs
import matplotlib.pyplot as plt
import time

# This script shows that the average time complexity for quicksort is O(n log n)
# while bubblesort has time complexity O(n^2).

def time_sort(vec, method):
    """
    This function takes a vector and sorting method as its input and outputs
    a vector with [the time it took to run the functions (in seconds), number
    of assignments made, number of conditionals made].
    """

    start = time.time()

    if method == "quick":
        x = algs.quicksort(vec)
    elif method == "bubble":
        x = algs.bubblesort(vec)

    return [time.time() - start, x[1], x[2]]

def transform(x,y):
    """
    This function takes an input vector of x values and y values, transforms them
    to return the y in a linearized format (assuming nlogn function was used
    to create y from x)
    """
    final = []
    for i in range(0, len(y)):
        new = y[i]#/x[i]
        final.append(2 ** new)

    return final

# Create vectors to compare runtime, assignments, and conditionals
quick_avg = []
bubble_avg = []

q_a_avg = []
b_a_avg = []

q_c_avg = []
b_c_avg = []

# Test the time each function takes to run on lists from 100 to 1000 in
# increments of 100
for i in np.arange(100,1001,100):

    # Average the results from 100 trials
    quick_trials = []
    bubble_trials = []

    q_assnmnt = []
    b_assnmnt = []

    q_cndtl = []
    b_cndtl = []

    for j in range(0, 100):

        # Test on a randomly-chosen vector of integers
        vec = np.random.randint(0, 2000, i)
        quick_trials.append(time_sort(vec, "quick")[0])
        bubble_trials.append(time_sort(vec, "bubble")[0])

        q_assnmnt.append(time_sort(vec, "quick")[1])
        b_assnmnt.append(time_sort(vec, "bubble")[1])

        q_cndtl.append(time_sort(vec, "quick")[2])
        b_cndtl.append(time_sort(vec, "bubble")[2])

    # Average the contents of the trials together, append to times
    quick_avg.append(sum(quick_trials)/len(quick_trials))
    bubble_avg.append(sum(bubble_trials)/len(bubble_trials))

    q_a_avg.append(sum(q_assnmnt)/len(q_assnmnt))
    b_a_avg.append(sum(b_assnmnt)/len(b_assnmnt))

    q_c_avg.append(sum(q_cndtl)/len(q_cndtl))
    b_c_avg.append(sum(b_cndtl)/len(b_cndtl))


# Print results
print('Q assignments: {}\nB assignments: {}\nQ conditionals: {}\nB conditionals: {}'.format(q_a_avg, b_a_avg, q_c_avg, b_c_avg))

# Make a graph showing time for the different types of input lists
x = np.arange(100, 1001, 100)

# Figure to show reference complexities
fig, ax = plt.subplots()
ax.plot(x, x * np.log2(x), label='log-linear')
ax.plot(x, x ** 2, label='n-squared')
#ax.plot(x, x, label='linear')
#ax.plot(x, np.log2(x), label='log')

ax.set(xlabel='x', ylabel='y',
       title='Reference Functions')
ax.grid()
ax.legend()

fig.savefig('output/reference.png', bbox_inches='tight')
fig.clf()

# Figure to show complexity of my algorithm
fig, ax = plt.subplots()
ax.plot(x, quick_avg, label='QuickSort time')
ax.plot(x, bubble_avg, label='BubbleSort time')

ax.set(xlabel='input vector length', ylabel='time to sort (s)',
       title='Algorithm Performance\n(average of 100 trials)')
ax.grid()
ax.legend()

fig.savefig('output/time.png', bbox_inches='tight')
fig.clf()

# Figure to show sqrt-transformed complexities
fig, ax = plt.subplots()
ax.plot(x, np.sqrt(quick_avg), label='QuickSort time')
ax.plot(x, np.sqrt(bubble_avg), label='BubbleSort time')

ax.set(xlabel='input vector length', ylabel='sqrt time to sort (sqrt(s))',
       title='Algorithm Performance\n(scaled)')
ax.grid()
ax.legend()

fig.savefig('output/sqrt-timed.png', bbox_inches='tight')
fig.clf()

# Figure to show exp-transformed complexities
fig, ax = plt.subplots()
ax.plot(x, transform(x,quick_avg), label='QuickSort time')
ax.plot(x, transform(x,bubble_avg), label='BubbleSort time')

ax.set(xlabel='input vector length', ylabel='exponent-transformed time to sort',
       title='Algorithm Performance\n(scaled)')
ax.grid()
ax.legend()

fig.savefig('output/exp-timed.png', bbox_inches='tight')
fig.clf()

# Figure to show assignments/conditionals
fig, ax = plt.subplots()
ax.plot(x, q_a_avg, label='QuickSort Assignments')
ax.plot(x, b_a_avg, label='BubbleSort Assignments')
ax.plot(x, q_c_avg, label='QuickSort Conditionals')
ax.plot(x, b_c_avg, label='BubbleSort Conditionals')

ax.set(xlabel='input vector length', ylabel='number of entities',
       title='Assignments & Conditionals')
ax.grid()
ax.legend()

fig.savefig('output/assignments.png', bbox_inches='tight')
fig.clf()
