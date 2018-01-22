import numpy as np
from sort import algs


def test_bubblesort():
    
    # 1) Test odd-sized vector + duplicate values
    assert algs.bubblesort([1,2,4,0,1]) == [0,1,1,2,4]

    # 2) Test even+duplicate values
    assert algs.bubblesort([1,2,4,6,0,1]) == [0,1,1,2,4,6]

    # 3) Test empty vector
    assert algs.bubblesort([]) == []

    # 4) Test single-element vectors
    assert algs.bubblesort([1]) == [1]

    # 5) Test single-value vectors
    assert algs.bubblesort([1,1,1,1,1,1,1,1]) == [1,1,1,1,1,1,1,1]

    # 6) Test vectors with negative values
    assert algs.bubblesort([-2,-6,8,9,-4]) == [-6,-4,-2,8,9]

    # 7) Test ordered and reverse-order lists of large size
    assert algs.bubblesort(range(1000)) == range(1000)
    assert algs.bubblesort(list(reversed(range(1000)))) == list(range(1000))

    # 8) Test vector of strings
    assert algs.bubblesort(["will", "this", "work"]) == ["this", "will", "work"]



def test_quicksort():

    # 1) Test odd-sized vector + duplicate values
    assert algs.quicksort([1,2,4,0,1]) == [0,1,1,2,4]

    # 2) Test even+duplicate values
    assert algs.quicksort([1,2,4,6,0,1]) == [0,1,1,2,4,6]

    # 3) Test empty vector
    assert algs.quicksort([]) == []

    # 4) Test single-element vectors
    assert algs.quicksort([1]) == [1]

    # 5) Test single-value vectors
    assert algs.quicksort([1,1,1,1,1,1,1,1]) == [1,1,1,1,1,1,1,1]

    # 6) Test vectors with negative values
    assert algs.quicksort([-2,-6,8,9,-4]) == [-6,-4,-2,8,9]

    # 7) Test ordered and reverse-order lists of large size
    assert algs.quicksort(range(1000)) == list(range(1000))
    assert algs.quicksort(list(reversed(range(1000)))) == list(range(1000))

    # 8) Test vector of strings
    assert algs.quicksort(["will", "this", "work"]) == ["this", "will", "work"]
