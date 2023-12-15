import numpy as np
import numpy.typing as npt
from typing import cast

def magicSum(n: int) -> int:
    return n * (n**2 + 1) // 2

def areMagicSums(sums: npt.NDArray[np.integer], ms: int) -> bool:
    """verify sums are magic according to magic sum ms

    Args:
        sums (npt.NDArray[np.integer]): 1D array of sums to check
        ms (np.integer): _description_

    Returns:
        bool: sums are all magic
    """
    return (sums == ms).all()

def isMagicForRows(square: npt.NDArray[np.integer], ms: int) -> bool:
    """verify square is magic for all its rows according to magic sum ms

    Args:
        square (npt.NDArray[np.integer]): square to check
        ms (np.integer): expected magic sum

    Returns:
        bool: whether the square is magic or not for its rows
    """
    sumRows = square.sum(axis=1)
    return areMagicSums(sumRows, ms)

def isMagicForColumns(square: npt.NDArray[np.integer], ms: int) -> bool:
    """verify square is magic for all its colums according to magic sum ms

    Args:
        square (npt.NDArray[np.integer]): square to check
        ms (np.integer): expected magic sum

    Returns:
        bool: whether the square is magic or not for its columns
    """
    sumColumns = square.sum(axis=0)
    return areMagicSums(sumColumns, ms)

def isMagicForDiagonals(square: npt.NDArray[np.integer], ms: int) -> bool:
    """verify square is magic for all its diagonals according to magic sum ms
    
    diagonals are: main diagonal and main diagonal of symetric square (vertical or horizontal)

    Args:
        square (npt.NDArray[np.integer]): square to check
        ms (np.integer): expected magic sum

    Returns:
        bool: whether the square is magic or not for its diagonals
    """
    trace1 = np.trace(square)
    trace2 = np.trace(square[::-1])
    # return areMagicSums(np.array([trace1, trace2]), ms)
    return (trace1 == ms) and (trace2 == ms)

def areAllPresent(square: npt.NDArray[np.integer], maxValue: int) -> bool:
    """verify that all numbers from 1 to maxValue are all used once

    Args:
        square (npt.NDArray[np.integer]): square to check
        maxValue (np.integer): maxValue in square

    Returns:
        bool: whether values are all used (once)
    """
    uniqueValues = np.unique(square)
    expectedValues = np.arange(1, maxValue+1)
    return (len(uniqueValues) == len(expectedValues)) \
        and  cast(bool, np.equal(uniqueValues, expectedValues).all())

def isMagic(square: npt.NDArray[np.integer]) -> bool:
    """verify square is magic with following rules:
    - sums of rows, columns, diagonals are the same
    - all numbers between 1 and n**2 are used once

    Args:
        square (np.ndarray): square to check
    Returns:
        bool: magicness of square
    """
    n = len(square)
    ms = magicSum(n)
    return areAllPresent(square, n**2) \
        and isMagicForRows(square, ms) \
        and isMagicForColumns(square, ms) \
        and isMagicForDiagonals(square, ms)
