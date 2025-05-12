class tarjetaCredito:
    '''clase que representa una tarjeta de credito'''
    def __init__(self, nombre_titular, banco, limite):
        self.__titulartitular = nombre_titular
        self.__banco = banco
        self.limite = limite
        self.__historial = []

    @property
    def limite(self):
      return self.__limite

    @limite.setter
    def limite(self, nuevo_limite):
        if isinstance(nuevo_limite, int) or isinstance(nuevo_limite, float):
            self.__limite = nuevo_limite
        else:
            self.__limite = 0.0

    @property
    def titular(self):
        return self.__titulartitular
    
    @property
    def historial(self):
        return self.__historial
    def compra(self, precio):
        if precio < self.__limite:
            self.__historial.append(-precio)
            return True
        else:
            return False
        
    def depositar(self, monto):
        if monto <= 0:
            return False
        else:
            self.__historial.append(monto)
            return True  
        
tarjeta_maximo = tarjetaCredito('maximo', 'Galicia', 1000000)
tarjeta_facundo = tarjetaCredito('facundo', 'Nacion', 500000)
tarjeta_pricila = tarjetaCredito('pricila', 'Santander', 2000000)


tarjeta_facundo.limite = 100
print(tarjeta_facundo.limite)
print(tarjeta_facundo.compra(50))
print(tarjeta_facundo.compra(150))

#---- Compras
tarjeta_pricila.compra(1000)
tarjeta_pricila.compra(500)
tarjeta_pricila.compra(1000)
#---- Deposito
tarjeta_pricila.depositar(100000000)

print(tarjeta_pricila.historial)
print(f"estado {sum(tarjeta_pricila.historial)}")