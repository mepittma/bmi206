import numpy as np

def bubblesort(vec):
    """
    x is an integer array of length 0 to j. bubblesort returns an array of
    length j in ascending order by swapping adjacent elements if they are not
    in the desired order.
    """

    # Outer loop: seq through each index of the given array
    for j in range(0, len(vec)-1):

        # Inner loop: if the element is greater than that of the next index, swap places
        for i in range(0,len(vec)-j-1):

            if vec[i] > vec[i+1]:
                vec[i], vec[i+1] = vec[i+1], vec[i]

    return vec

def quicksort(vec):
    """
    x is an integer array of length 0 to i. quicksort returns an array of length i
    in ascending order by recursively partitioning around a pivot until all
    elements are in the desired order.
    """

    # Initialize vectors to hold partitioned values
    left = []
    right = []
    equal = []

    # Only run if vector contains elements
    if len(vec) > 1:

        # Pick a pivot (first element in the vector)
        q = vec[int(len(vec)/2)]

        # Scan through the vector, assigning each element to new vectors
        # based on whether it is larger or smaller than the partition
        for i  in range(0, len(vec)-1):
            if vec[i] < q:
                left.append(vec[i])
            elif vec[i] == q:
                equal.append(vec[i])
            else:
                right.append(vec[i])

        # Do this recursively to the partitioned vectors
        return quicksort(left) + equal + quicksort(right)

    # in the case of empty vectors, just return it
    else:
        return vec
