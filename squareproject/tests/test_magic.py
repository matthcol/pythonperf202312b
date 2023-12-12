import pytest
from magic import magicSum, isMagic

def test_magicSum_3():
    n = 3
    ms = magicSum(n)
    assert ms == 15
    
@pytest.mark.parametrize(
    argnames=["n", "msExpected"],
    argvalues=[
        (1, 1),
        (3, 15),
        (4, 34),
        (5, 65),
        (8, 260),
        (12, 870),  
    ]
)
def test_magicSum(n, msExpected):
    msActual = magicSum(n)
    assert msActual == msExpected
    
    
def test_isMagic_ok_3(square_ok_3):
    assert isMagic(square_ok_3)