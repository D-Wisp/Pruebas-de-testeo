
"""
Resumen de Programación Orientada a Objetos (OOP) en Python.
"""

# ============================================
# DEFINICIÓN DE UNA CLASE BÁSICA
# ============================================

class Persona:
    """Clase que representa una persona."""
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo

    def saludar(self):
        """Método que imprime un saludo."""
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear una instancia
persona1 = Persona("Lucía", 25)
persona1.saludar()

# ============================================
# ENCAPSULACIÓN (atributos "privados")
# ============================================

class CuentaBancaria:
    """Clase que simula una cuenta bancaria."""
    def __init__(self, titular, saldo):
        self.titular = titular
        self._saldo = saldo  # Atributo "privado" (por convención)

    def ver_saldo(self):
        print(f"Saldo de {self.titular}: ${self._saldo}")

cuenta = CuentaBancaria("Pedro", 1000)
cuenta.ver_saldo()

# ============================================
# DUCK TYPING
# ============================================

class Pato:
    def hacer_sonido(self):
        print("¡Cuac cuac!")

class Perro:
    def hacer_sonido(self):
        print("¡Guau guau!")

# Función que no importa el tipo de objeto

def hacer_sonar(animal):
    animal.hacer_sonido()

pato = Pato()
perro = Perro()
hacer_sonar(pato)
hacer_sonar(perro)

# ============================================
# SOBRECARGA DE OPERADORES
# ============================================

class NumeroEspecial:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, otro):
        return NumeroEspecial(self.valor + otro.valor + 10)  # Suma especial

    def __str__(self):
        return f"Valor: {self.valor}"

n1 = NumeroEspecial(5)
n2 = NumeroEspecial(3)
resultado = n1 + n2
print(resultado)

# ============================================
# ITERADORES MANUALES
# ============================================

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.actual = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.actual < self.limite:
            self.actual += 1
            return self.actual
        else:
            raise StopIteration

contador = Contador(3)
for numero in contador:
    print(numero)


# ITERADORES AUTOMÁTICOS


class MiLista:
    def __init__(self, datos):
        self.datos = datos

    def __len__(self):
        return len(self.datos)

    def __getitem__(self, indice):
        return self.datos[indice]

mi_lista = MiLista([10, 20, 30])
for valor in mi_lista:
    print(valor)


# FIN DEL RESUMEN


"""
Este resumen cubre:
- Definición de clases, objetos, atributos y métodos.
- Encapsulación (usando guiones bajos).
- Duck Typing.
- Sobrecarga de operadores.
- Iteradores manuales y automáticos.
"""
