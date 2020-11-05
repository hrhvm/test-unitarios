import pytest
from TresNumeros import TresNumeros


def testOrdenar():
    op = TresNumeros()

    n1,n2,n3= op.ordenar(7,3,1)
    assert(1)==n1
    assert(3)==n2
    assert(7)==n3

@pytest.mark.parametrize(
    "n1,n2,n3,expected_n1,expected_n2,expected_n3",[
        (9,8,4,4,8,9),
        (7,3,1,1,3,7),
    ]
)
def test_ordenarVarios(n1,n2,n3,expected_n1,expected_n2,expected_n3):
    op = TresNumeros()
    num1,num2,num3 = op.ordenar(n1,n2,n3)
    assert(expected_n1)==num1
    assert(expected_n2)==num2
    assert(expected_n3)==num3
