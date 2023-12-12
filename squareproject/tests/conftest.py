import numpy as np
import pytest

@pytest.fixture
def square_ok_3():
    return np.array(
    [[8,1,6],
     [3,5,7], 
     [4,9,2]]
)