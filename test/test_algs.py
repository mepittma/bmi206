import numpy as np
from sort import algs


def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    # 1) Test odd-sized vector + duplicate values
    x = np.array([1,2,4,0,1])
    y = algs.bubblesort(x)
    assert y == np.array([0,1,1,2,4])

    # 2) Test even+duplicate values
    x = np.array([1,2,4,0,1,4])
    y = algs.bubblesort(x)
    assert y == np.array([0,1,1,2,4,4])

    # 3) Test empty vector
    x = np.array([])
    y = algs.bubblesort(x)
    assert y == np.array([])

    # 4) Test single-element vectors
    x = np.array([1])
    y = algs.bubblesort(x)
    assert y == np.array([1])

    # 5) Test single-value vectors
    x = np.array([1,1,1,1,1,1,1,1,1])
    y = algs.bubblesort(x)
    assert y == np.array([1,1,1,1,1,1,1,1,1])

    # 6) Test vector of strings
    x = ["will", "this", "work"]
    y = algs.bubblesort(x)
    assert y == ["this", "will", "work"]


def test_quicksort():

    # 1) Test odd-sized vector + duplicate values
    x = np.array([1,2,4,0,1])
    y = algs.quicksort(x)
    assert y == np.array([0,1,1,2,4])

    # 2) Test even+duplicate values
    x = np.array([1,2,4,0,1,4])
    y = algs.quicksort(x)
    assert y == np.array([0,1,1,2,4,4])

    # 3) Test empty vector
    x = np.array([])
    y = algs.quicksort(x)
    assert y == np.array([])

    # 4) Test single-element vectors
    x = np.array([1])
    y = algs.quicksort(x)
    assert y == np.array([1])

    # 5) Test single-value vectors
    x = np.array([1,1,1,1,1,1,1,1,1])
    y = algs.quicksort(x)
    assert y == np.array([1,1,1,1,1,1,1,1,1])

    # 6) Test vector of strings
    x = ["will", "this", "work"]
    y = algs.quicksort(x)
    assert y == ["this", "will", "work"]
