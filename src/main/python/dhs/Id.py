from enum import Enum

class TipoDato(Enum):
    VOID = "void"
    INT = 'int'
    FLOAT = 'float'
    BOOLEAN = 'bool' 
    DOUBLE = 'double'
    CHAR = 'char'
    ERROR = 'error' # Tipo para propagar errores

    @staticmethod
    def esNumerico(tipo):
        return tipo in [TipoDato.INT, TipoDato.FLOAT, TipoDato.DOUBLE]

class ID():
    def __init__(self, nombre, tD, inicializado, usado):
        self.nombre = nombre
        # Convertimos el string del parser al Enum
        if isinstance(tD, str):
            try:
                self.tipoDato = TipoDato(tD.lower())
            except ValueError:
                self.tipoDato = TipoDato.VOID
        else:
            self.tipoDato = tD
        self.inicializado = inicializado
        self.usado = usado

    def __str__(self):
        return(f"ID: \t{self.nombre}\t{self.tipoDato}\tInicializado:{self.inicializado}\t Usado:{self.usado}")

    def isUsado(self):
         return self.usado == 1

class Variable(ID):
    def __init__(self, nombre, tipoDatoVariable, inicializado, usado):
        super().__init__(nombre, tipoDatoVariable, inicializado, usado)

class Funcion(ID):
    def __init__(self, nombre, tipoDato, inicializado, usado, args):
        super().__init__(nombre, tipoDato, inicializado, usado)
        self.args = args