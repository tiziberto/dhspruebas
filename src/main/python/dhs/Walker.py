from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

#Esto recorre nodo por nodo basicamente
class Walker (compiladoresVisitor) :

    temporales = 0
    etiquetas = 0




    #Comenzamos recorriendo el programa
    #--------------------------------------------------------------
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("=-"*20)
        print("--Comienza a caminar--")
        self.visitInstrucciones(ctx.getChild(0))
        print("Fin del Recorrido")

    #Comenzamos con las declaraciones
    #------------------------------------------------------------
    def visitInit(self, ctx):
        #Podemos hacer la declaracion de varias variables a la vez, la recorremos
        print("=-"*20)
        print("SE ENCONTRO UNA DECLARACION")
        print("=-"*20)
        for i in range(1, ctx.getChildCount()):
            nombre = ctx.getChild(i)
            if hasattr(nombre, 'symbol') and nombre.symbol.type == compiladoresParser.ID:
                variable = nombre.getText()
                print("Variable: " + variable)
        print("=-"*20)
        #print (ctx.getChild(0).getText()+" - "+ctx.getChild(1))
        #return none
    
   # def visitBloque(self, ctx:compiladoresParser.BloqueContext):
    #    print("Nuevo Programa")
     #   return super().visitInstrucciones(ctx.getChild(1))

    def visitTerminal(self, node):
        print(" ==> Token "+ node.getText())
        return super().visitTerminal(node)
    
    def visitInstrucciones(self, ctx: compiladoresParser.InstruccionesContext):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            
            if hasattr(child, 'getRuleIndex') and not isinstance(child, compiladoresParser.InstruccionesContext):
                self.visit(child)
            elif isinstance(child, compiladoresParser.InstruccionesContext):
                self.visit(child)

    def visitInstruccion(self, ctx:compiladoresParser.InstruccionContext):
    # Despacha a la instrucción específica (declaración, asignación, etc.)
        if ctx.puntoYComa():
            return self.visitPuntoYComa(ctx.puntoYComa())
        elif ctx.iwhile():
            return self.visitIwhile(ctx.iwhile())
        elif ctx.bloque():
            return self.visitBloque(ctx.bloque())
        elif ctx.ifor():
            return self.visitIfor(ctx.ifor())
        elif ctx.func():
            return self.visitFunc(ctx.func())
        elif ctx.IF():  
            return self.visitIf(ctx.if_())

    def visitIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("=-"*20)
        print("SE ENCONTRO UN WHILE")
        print("=-"*20)
        
        if ctx.opal():
            condicion = self.obtenerValor(ctx.opal())
            print(f"Condición: {condicion}")
        
        print("Cuerpo del while:")

        if ctx.bloque():
            self.visitBloque(ctx.bloque())
        else:
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if hasattr(child, 'getRuleIndex') and isinstance(child, compiladoresParser.InstruccionContext):
                    self.visit(child)
        
        print("=-"*20)



    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        print("=-"*20)
        print("SE ENCONTRO UNA ASIGNACION")
        print("=-"*20)
        variable = ctx.ID().getText()
        if ctx.opal():
            # Procesa la expresión/operación
            valor = self.obtenerValor(ctx.opal())
            print(variable +" = " + f" {valor}")
        elif ctx.char():
            # Procesa el carácter
            char_valor = ctx.char().getText()
            print(variable +" = " + f" {char_valor}")
        print("=-"*20)

    def obtenerValor(self, ctx):
        """Extrae el texto/valor de una operación o expresión"""
        return ctx.getText()