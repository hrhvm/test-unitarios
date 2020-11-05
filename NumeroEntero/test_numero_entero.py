
from NumeroEntero import NumeroEntero


def testCocienteResiduo():

    entero = NumeroEntero()
    cociente,residuo = entero.division(6,6)
    
    assert(1)==cociente
    assert(0)==residuo
