import numpy as np

def bubblesort(vec):
    """
    x is an integer array of length 0 to j. bubblesort returns an array of
    length j in ascending order by swapping adjacent elements if they are not
    in the desired order.
    """

    assnmnt = 0
    cndtl = 0

    # Outer loop: seq through each index of the given array
    for j in range(0, len(vec)-1):

        # Inner loop: if the element is greater than that of the next index, swap places
        for i in range(0,len(vec)-j-1):



            if vec[i] > vec[i+1]:
                vec[i], vec[i+1] = vec[i+1], vec[i]; assnmnt += 2

    return [vec, assnmnt, cndtl]

def quicksort(vec):
    """
    x is an integer array of length 0 to i. quicksort returns a list with
    [1] array of length i in ascending order
    [2] number of assignments made during the function call
    [3] number of conditionals evaluated in the function call.

    QuickSort works by recursively partitioning around a pivot until all
    elements are in the desired order.
    """

    assnmnt = 0
    cndtl = 0

    # Initialize vectors to hold partitioned values
    left = []; assnmnt += 1
    right = []; assnmnt += 1
    equal = []; assnmnt += 1

    # Only run if vector contains elements
    cndtl += 1
    if len(vec) > 1:

        # Pick a pivot (first element in the vector)
        q = vec[int(len(vec)/2)]; assnmnt += 1

        # Scan through the vector, assigning each element to new vectors
        # based on whether it is larger or smaller than the partition
        i = 0; assnmnt += 1
        while i < len(vec):

            cndtl += 1
            if vec[i] < q:
                left.append(vec[i])

            cndtl += 1
            elif vec[i] == q:
                equal.append(vec[i])

            cndtl += 1
            else:
                right.append(vec[i])
            i = i+1

        # Do this recursively to the partitioned vectors
        return quicksort(left) + equal + quicksort(right)

    # in the case of empty vectors, just return it
    else:
        return [vec, assnmnt, cndtl]
