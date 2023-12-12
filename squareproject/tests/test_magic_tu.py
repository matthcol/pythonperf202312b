import pytest
from magic import *

# areMagicSums

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
    
# areAllPresent

@pytest.mark.parametrize(["squareName", "maxValue"], [
    ("square_ok_3", 9), 
    ("square_ko_3_row", 9), 
    ("square_ko_3_col", 9), 
    ("square_ko_3_diag", 9),
    ("square_ok_5", 25), 
    ("square_ok_8_benjamin_franklin", 64),
    ("square_ok_4_albrecht_durer", 16),
    ("square_ok_5_semi_diabolik", 25),
    ("square_ok_8_general_cazalas", 64), 
    ("square_ok_8_willem_barink", 64),
    ("square_ok_12_willem_barink", 144),
])
def test_areAllPresent_ok(squareName, maxValue, request):
    square = request.getfixturevalue(squareName)
    assert areAllPresent(square, maxValue)
    
@pytest.mark.parametrize(["squareName", "maxValue"], [
    ("square_ko_4_josep_maria_subirachs", 16),
])
def test_areAllPresent_ko(squareName, maxValue, request):
    square = request.getfixturevalue(squareName)
    assert not areAllPresent(square, maxValue)

