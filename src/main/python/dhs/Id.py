from enum import Enum

class TipoDato(Enum):
        VOID = "void"
        INT = 'int'
        FLOAT = 'float'
        BOOLEAN = 'bool' 
        DOUBLE = 'double'
        CHAR = 'char'
        ERROR = 'error'

class ID():
    
    def __init__(self,nombre,tD,inicializado,usado):
        self.nombre=nombre
        self.tipoDato=TipoDato(tD)
        self.inicializado=inicializado
        self.usado=usado

    def __str__(self):
        return("ID: \t"+self.nombre+"\t"+str(self.tipoDato)+"\tInicializado:"+str(self.inicializado)+ "\t Usado:"+str(self.usado))

    def isUsado(self):
         
         return self.usado == 1

class Variable(ID):
    def __init__(self, nombre, tipoDatoVariable, inicializado=0, usado=0):
        super().__init__(nombre, tipoDatoVariable, inicializado, usado)



class Funcion(ID):
    def __init__(self, nombre, tipoDato, args):
        super().__init__(nombre, tipoDato, 1, 0)
        self.args = args
