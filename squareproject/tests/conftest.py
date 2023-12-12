import numpy as np
import numpy.typing as npt
import pytest

@pytest.fixture
def square_ok_3() -> npt.NDArray[np.integer]:
    return np.array(
            [[8,1,6],
            [3,5,7], 
            [4,9,2]]
    )
    
@pytest.fixture
def square_ko_3_row() -> npt.NDArray[np.integer]:
    return np.array( 
            [[8,9,6],
            [3,5,7],
            [4,1,2]]
    )

@pytest.fixture
def square_ko_3_col() -> npt.NDArray[np.integer]:
    return np.array(
            [[8,1,6], 
            [7,5,3], 
            [4,9,2]]
    )

@pytest.fixture
def square_ko_3_diag() -> npt.NDArray[np.integer]: 
    return np.array([
        [8,1,6],
        [4,9,2],
        [3,5,7]
    ])

@pytest.fixture
def square_ok_4() -> npt.NDArray[np.integer]: 
    return np.array([[1,	24,	3,	25,	12],
		[16,	7,	21,	6,	15],
		[23,	14,	18,	8,	2],
		[5,		9,	10,	22,	19],
		[20,	11,	13,	4,	17]])

@pytest.fixture
def square_ok_4_albrecht_durer() -> npt.NDArray[np.integer]: 
    return  np.array([[16,	3,	2,	13], [5, 10, 11, 8],[9, 6, 7, 12], [4, 15,	14,	1]])
 
@pytest.fixture
def square_ko_4_josep_maria_subirachs() -> npt.NDArray[np.integer]: 
    """magic square from 'la Sagrada Familia' in Barcelona

    Returns:
        _type_: _description_
    """
    return np.array(
        [[1	,14,	14,	4],
        [11,	7,	6,	9],
        [8,	10,	10,	5],
        [13,	2,	3,	15]]
    ) 	

@pytest.fixture
def square_ok_5_semi_diabolik():
    return np.array(
            [[17,	24,	1,	8,	15],
            [23,	5,	7,	14,	16],
            [4,	6,	13,	20,	22],
            [10,	12,	19,	21,	3],
            [11,	18,	25,	2,	9]]
    )

@pytest.fixture
def square_ok_8_benjamin_franklin():
    return np.array(
            [[52,	61,	4,	13,	20,	29,	36,	45],
            [14,	3,	62,	51,	46,	35,	30,	19],
            [53,	60,	5,	12,	21,	28,	37,	44],
            [11,	6,	59,	54,	43,	38,	27,	22],
            [55,	58,	7,	10,	23,	26,	39,	42],
            [9,		8,	57,	56,	41,	40,	25,	24],
            [50,	63,	2,	15,	18,	31,	34,	47],
            [16,	1,	64,	49,	48,	33,	32,	17]]
    )

@pytest.fixture
def square_ok_8_general_cazalas():
    return  np.array(
            [[1,	8,	53,	52,	45,	44,	25,	32],
            [64,	57,	12,	13,	20,	21,	40,	33],
            [2,	7,	54,	51,	46,	43,	26,	31],
            [63,	58,	11,	14,	19,	22,	39,	34],
            [3,	6,	55,	50,	47,	42,	27,	30],
            [62,	59,	10,	15,	18,	23,	38,	35],
            [4,	5,	56,	49,	48,	41,	28,	29],
            [61,	60,	9,	16,	17,	24,	37,	36]]
    )

@pytest.fixture
def square_ok_8_willem_barink():
    return  np.array(
            [[60,	6,	11,	53,	44,	22,	27,	37],
            [13,	51,	62,	4,	29,	35,	46,	20],
            [54,	12,	5,	59,	38,	28,	21,	43],
            [3,	61,	52,	14,	19,	45,	36,	30],
            [58,	8,	9,	55,	42,	24,	25,	39],
            [15,	49,	64,	2,	31,	33,	48,	18],
            [56,	10,	7,	57,	40,	26,	23,	41],
            [1,	63,	50,	16,	17,	47,	34,	32]]
    )

@pytest.fixture
def square_ok_12_willem_barink_12():
    return np.array( 
            [[138,	8,	17,	127,	114,	32,	41,	103,	90,	56,	65,	79],
            [19,	125,	140,	6,	43,	101,	116,	30,	67,	77,	92,	54],
            [128,	18,	7,	137,	104,	42,	31,	113,	80,	66,	55,	89],
            [5,	139,	126,	20,	29,	115,	102,	44,	53,	91,	78,	68],
            [136,	10,	15,	129,	112,	34,	39,	105,	88,	58,	63,	81],
            [21,	123,	142,	4,	45,	99,	118,	28,	69,	75,	94,	52],
            [130,	16,	9,	135,	106,	40,	33,	111,	82,	64,	57,	87],
            [3,	141,	124,	22,	27,	117,	100,	46,	51,	93,	76,	70],
            [134,	12,	13,	131,	110,	36,	37,	107,	86,	60,	61,	83],
            [23,	121,	144,	2,	47,	97,	120,	26,	71,	73,	96,	50],
            [132,	14,	11,	133,	108,	38,	35,	109,	84,	62,	59,	85],
            [1,	143,	122,	24,	25,	119,	98,	48,	49,	95,	74,	72]]
    )