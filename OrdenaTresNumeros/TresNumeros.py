
class TresNumeros():

    def ordenar(self,n1,n2,n3):
        sw = True 
        
        while sw==True:
            sw=False
            if n1>n2:
                n1,n2=self.__cambiar(n1,n2)
                sw=True
            
            if n2>n3:
                n2,n3=self.__cambiar(n2,n3)
                sw=True
        return n1,n2,n3

    def __cambiar(self,x,y):
        temp = x
        x=y
        y=temp
        return x,y
