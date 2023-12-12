import numpy as np

def magicSum(n):
    return n * (n**2 + 1) // 2


def isMagic(square: np.ndarray) -> bool:
    """verify square is magic with following rules:
    - sums of rows, columns, diagonals are the same
    - all numbers between 1 and n**2 are used once

    Args:
        square (np.ndarray): square to check
    Returns:
        bool: magicness of square
    """
    return False