import pytest
from magic import *
from .constants import *


# isMagicForRows

@pytest.mark.parametrize(["squareName","ms"], [
    ("square_ok_3", MS_3), 
    ("square_ko_3_col", MS_3), 
    ("square_ko_3_diag", MS_3), 
    ("square_ok_5", MS_5), 
    ("square_ok_4_albrecht_durer", MS_4),
    ("square_ok_5_semi_diabolik", MS_5),
    ("square_ok_8_general_cazalas", MS_8), 
    ("square_ok_8_willem_barink", MS_8),
    ("square_ok_12_willem_barink", MS_12),
    ("square_ko_4_josep_maria_subirachs", 33)
])
def test_isMagicForRows_ok(squareName, ms, request):
    square = request.getfixturevalue(squareName)
    assert isMagicForRows(square, ms)
    
@pytest.mark.parametrize(["squareName","ms"], [
    ("square_ko_3_row", MS_3), 
])
def test_isMagicForRows_ko(squareName, ms, request):
    square = request.getfixturevalue(squareName)
    assert not isMagicForRows(square, ms)

# isMagicForColumns

@pytest.mark.parametrize(["squareName","ms"], [
    ("square_ok_3", MS_3), 
    ("square_ko_3_row", MS_3), 
    ("square_ko_3_diag", MS_3), 
    ("square_ok_5", MS_5), 
    ("square_ok_12_willem_barink", MS_12),
    ("square_ko_4_josep_maria_subirachs", 33)
])
def test_isMagicForColumns_ok(squareName, ms, request):
    square = request.getfixturevalue(squareName)
    assert isMagicForColumns(square, ms)
    
@pytest.mark.parametrize(["squareName","ms"], [
    ("square_ko_3_col", MS_3), 
])
def test_isMagicForColumns_ko(squareName, ms, request):
    square = request.getfixturevalue(squareName)
    assert not isMagicForColumns(square, ms)

# isMagicForDiagonals

@pytest.mark.parametrize(["squareName","ms"], [
    ("square_ok_3", MS_3), 
    ("square_ko_3_row", MS_3), 
    ("square_ko_3_col", MS_3),  
    ("square_ok_5", MS_5), 
    ("square_ok_12_willem_barink", MS_12),
    ("square_ko_4_josep_maria_subirachs", 33)
])
def test_isMagicForDiagonals_ok(squareName, ms, request):
    square = request.getfixturevalue(squareName)
    assert isMagicForDiagonals(square, ms)
    
@pytest.mark.parametrize(["squareName","ms"], [
    
    ("square_ko_3_diag", MS_3),
    ("square_ko_3_diag_one", MS_3),
    ("square_ko_3_diag_two", MS_3),
])
def test_isMagicForDiagonals_ko(squareName, ms, request):
    square = request.getfixturevalue(squareName)
    assert not isMagicForDiagonals(square, ms)


# all criteria

@pytest.mark.parametrize("squareName", [
    "square_ok_3", 
    "square_ok_5",
    "square_ok_4_albrecht_durer",
    "square_ok_5_semi_diabolik",
    "square_ok_8_general_cazalas", 
    "square_ok_8_willem_barink",
    "square_ok_12_willem_barink"
])
def test_isMagic_ok(squareName, request):
    square = request.getfixturevalue(squareName)
    assert isMagic(square)
    
    
@pytest.mark.parametrize("squareName", [
    "square_ko_3_col",
    "square_ko_3_row",
    "square_ko_3_diag", 
    "square_ok_8_benjamin_franklin",
    "square_ko_4_josep_maria_subirachs",
])
def test_isMagic_ko(squareName, request):
    square = request.getfixturevalue(squareName)
    assert not isMagic(square)