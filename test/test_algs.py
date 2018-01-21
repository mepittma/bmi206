import numpy as np
from sort import algs


def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

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

    # 6) Test vector of strings
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

    # 6) Test vector of strings
    assert algs.quicksort(["will", "this", "work"]) == ["this", "will", "work"]
