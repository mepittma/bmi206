b_assnmnt = 0
b_cndtl = 0

q_assnmnt = 0
q_cndtl = 0

def bubblesort(vec):
    """
    x is an integer array of length 0 to j. bubblesort returns an array of
    length j in ascending order by swapping adjacent elements if they are not
    in the desired order.
    """

    global b_assnmnt
    global b_cndtl

    # Outer loop: seq through each index of the given array
    for j in range(0, len(vec)-1):

        # Inner loop: if the element is greater than that of the next index, swap places
        for i in range(0,len(vec)-j-1):

            b_cndtl += 1
            if vec[i] > vec[i+1]:
                vec[i], vec[i+1] = vec[i+1], vec[i]
                b_assnmnt += 2

    return [vec, b_assnmnt, b_cndtl]

def quicksort(vec):
    """
    x is an integer array of length 0 to i. quicksort returns a list with
    [1] array of length i in ascending order
    [2] number of assignments made during the function call
    [3] number of conditionals evaluated in the function call.

    QuickSort works by recursively partitioning around a pivot until all
    elements are in the desired order.
    """

    global q_assnmnt
    global q_cndtl

    # Initialize vectors to hold partitioned values
    left = []
    right = []
    equal = []
    q_assnmnt += 3

    # Only run if vector contains elements
    q_cndtl += 1
    if len(vec) > 1:

        # Pick a pivot (first element in the vector)
        q = vec[int(len(vec)/2)]
        q_assnmnt += 1

        # Scan through the vector, assigning each element to new vectors
        # based on whether it is larger or smaller than the partition
        i = 0
        q_assnmnt += 1
        while i < len(vec):

            q_cndtl += 1
            if vec[i] < q:
                left.append(vec[i])

            elif vec[i] > q:
                right.append(vec[i])
                q_cndtl += 1

            else:
                equal.append(vec[i])
                q_cndtl += 1

            i += 1
            q_assnmnt += 1

        # Do this recursively to the partitioned vectors
        return [quicksort(left)[0] + equal + quicksort(right)[0], q_assnmnt, q_cndtl]

    # in the case of empty vectors, just return it
    else:
        return [vec, q_assnmnt, q_cndtl]
