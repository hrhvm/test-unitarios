class NumeroEntero():

    def division(self,dividendo, divisor):
        cociente = 0
       
        while dividendo>=divisor:
            dividendo -= divisor
            cociente +=1 
            
        residuo = dividendo

        return cociente,residuo
