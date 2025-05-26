## Clase que represente a un empleado 
## Atributos
## Apellido -> Alfanumérico y no tiene que contener números
## Nombres -> Alfanumérico y no tiene que contener números
## Fecha nacimiento -> Año, mes, dia tiene que ser una fecha válida,
##                  Al momento de la creación del objeto debe tener 18 años o más
## Género -> M, F, X 
## Fecha de alta -> Año, mes, día tiene que ser una fecha válida, 
##                 no puede ser menor que la fecha nacimiento
## Sueldo base   -> Float, no puede ser menor a cero

class empleado:
    def __init__(self):
        self.apellido = True
        self.nombres = True
        self.fecha_nacimiento = True
        self.genero = True
        self.fecha_alta = True
        self.sueldo_base = True

    @property
    def sueldo_base(self):
        return self.__sueldo_base
    
    @sueldo_base.setter
    def sueldo_base(self, sueldo):
        if sueldo < 0:
            raise ValueError(f"el sueldo no puede ser negativo: {sueldo}")
        self.__sueldo_base = sueldo
        
        
empleado1 = empleado(-10.00)