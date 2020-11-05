from TresNumeros import TresNumeros

from OrdenarTresNumerosIf import OrdenarTresNumeros

### ejemplo usando ordenar 3 numero con while

def ordenar_while():
    op = TresNumeros()
    ordenado= op.ordenar(5,4,3)
    print(ordenado)

#### fin ejemplo ordenar 3 numeros con while


### ejemplo usando ordenar 3 numero con if

def ordenar_if():
    op = OrdenarTresNumeros()
    ordenado = op.ordenar(3,2,6)
    print (ordenado )

### fin ejemplo ordenar 3 numeros con if

if __name__=="__main__":
    ordenar_while()

    #ordenar_if()