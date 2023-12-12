import pytest
from magic import *

@pytest.mark.parametrize(
    argnames=["sums", "ms"],
    argvalues=[
        (np.array([1]), 1),
        (np.array([15,15,15]), 15),
    ]
)
def test_areMagicSums_ok(sums, ms):
    assert areMagicSums(sums, ms)
    
@pytest.mark.parametrize(
    argnames=["sums", "ms"],
    argvalues=[
        (np.array([1]), 2),
        (np.array([16,15,15]), 15),
        (np.array([15,16,15]), 15),
        (np.array([15,15,16]), 15),
        (np.array([16,16,15]), 15),
        (np.array([16,15,16]), 15),
        (np.array([15,16,16]), 15),
        (np.array([16,16,16]), 15),
    ]
)
def test_areMagicSums_ko(sums, ms):
    assert not areMagicSums(sums, ms)