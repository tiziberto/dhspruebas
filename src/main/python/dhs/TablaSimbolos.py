from Contexto import Contexto
from Id import ID
class TablaSimbolos(object):

    __instance= None 
    contextos=[]   
    

    def __new__(cls):
        if TablaSimbolos.__instance is None:
            TablaSimbolos.__instance = object.__new__(cls)
        return TablaSimbolos.__instance
    
    def __init__(self) :
        contextoGlobal= Contexto()
        self.contextos.append(contextoGlobal)

    def addContexto(self,contexto):
        self.contextos.append(contexto) 

    def delContexto(self):
        self.contextos.pop()

    def addIdentificador(self,nombre,tipoDato):
        contexto=self.contextos[-1]
        id = ID(nombre,tipoDato,0,0)
        contexto.tabla.update({nombre:id})


    def buscarLocal(self, nombre):
        resultadoBusqueda = self.contextos[-1].traerVariable(nombre)
        if (resultadoBusqueda) == None:
            return 1

        else:
            return resultadoBusqueda


    
    def buscarGlobal(self, nombre):
        resultadoBusqueda = self.contextos[0].traerVariable(nombre)
        if (resultadoBusqueda) == None:
            return 1
        
        else :
            return resultadoBusqueda
    


    

    #def addIdentificador(self,tipo,nombreVariable):