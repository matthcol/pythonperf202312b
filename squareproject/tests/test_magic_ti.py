import pytest
from magic import *

@pytest.mark.parametrize("squareName", [
    "square_ok_3", 
    "square_ok_4", 
    "square_ok_12_willem_barink_12"
])
def test_isMagic_ok(squareName, request):
    square = request.getfixturevalue(squareName)
    assert isMagic(square)
    
    
@pytest.mark.parametrize("squareName", [
    "square_ko_3_col",
    "square_ko_3_row",
    "square_ko_3_diag", 
])
def test_isMagic_ko(squareName, request):
    square = request.getfixturevalue(squareName)
    assert not isMagic(square)