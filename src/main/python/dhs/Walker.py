from compiladoresVisitor import compiladoresVisitor
from compiladoresParser import compiladoresParser

#Esto recorre nodo por nodo basicamente
class Walker (compiladoresVisitor) :

    temporales = 0
    etiquetas = 0
    codigo_intermedio = []  # Lista para guardar el código de 3 direcciones




    #Comenzamos recorriendo el programa
    #--------------------------------------------------------------
    def visitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("=-"*20)
        print("--Comienza a caminar--")
        self.visitInstrucciones(ctx.getChild(0))
        print("Fin del Recorrido")
        # Mostrar el código de 3 direcciones generado
        self.mostrarCodigoIntermedio()

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
    
    def visitBloque(self, ctx:compiladoresParser.BloqueContext):
        print("  [Entrando a bloque]")
        return self.visitInstrucciones(ctx.getChild(1))

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
        elif ctx.if_():  
            return self.visitIf(ctx.if_())

    
    
    #While anda bien
    def visitIwhile(self, ctx:compiladoresParser.IwhileContext):
        print("=-"*20)
        print("SE ENCONTRO UN WHILE")
        print("=-"*20)
        
     
        etiqueta_inicio = self.generarEtiqueta()
        etiqueta_salida = self.generarEtiqueta()
        self.agregarCodigo(f"{etiqueta_inicio}:")
        
        if ctx.opal():
            condicion = self.procesarOpal(ctx.opal())
            print(f"Condición: {condicion}")
            self.agregarCodigo(f"if NOT ({condicion}) goto {etiqueta_salida}")
        
        print("Cuerpo del while:")

        if ctx.bloque():
            self.visitBloque(ctx.bloque())
        else:
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if hasattr(child, 'getRuleIndex') and isinstance(child, compiladoresParser.InstruccionContext):
                    self.visit(child)
        
       
        self.agregarCodigo(f"goto {etiqueta_inicio}")
        self.agregarCodigo(f"{etiqueta_salida}:")
        
        print("=-"*20)


    def visitIf(self, ctx:compiladoresParser.IfContext):
        print("=-"*20)
        print("SE ENCONTRO UN IF")
        print("=-"*20)
        
        etiqueta_else = self.generarEtiqueta()
        etiqueta_fin = self.generarEtiqueta()
        
        if ctx.opal():
            condicion = self.procesarOpal(ctx.opal())
            print(f"Condición: {condicion}")
            self.agregarCodigo(f"if NOT ({condicion}) goto {etiqueta_else}")
        
        print("Cuerpo del IF:")

        if ctx.bloque():
            self.visitBloque(ctx.bloque())
        else:
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if hasattr(child, 'getRuleIndex') and isinstance(child, compiladoresParser.InstruccionContext):
                    self.visit(child)
        
   
        self.agregarCodigo(f"goto {etiqueta_fin}")

        self.agregarCodigo(f"{etiqueta_else}:")
        
        if ctx.else_().ELSE():
            self.visitElse(ctx.else_())
        
 
        self.agregarCodigo(f"{etiqueta_fin}:")
        
        print("=-"*20)

    def visitElse(self, ctx:compiladoresParser.ElseContext):
        print("=-"*20)
        print("SE ENCONTRO UN ELSE")
        print("=-"*20)
        
        if ctx.bloque():
            print("Cuerpo del ELSE:")
            self.visitBloque(ctx.bloque())
        
        elif ctx.if_():
            print("ELSE IF:")
            self.visitIf(ctx.if_())
        
        print("=-"*20)

    def visitIfor(self, ctx:compiladoresParser.IforContext):
        print("=-"*20)
        print("SE ENCONTRO UN FOR")
        print("=-"*20)
        
        etiqueta_inicio = self.generarEtiqueta()
        etiqueta_salida = self.generarEtiqueta()

        if ctx.asignacion():
            asignacion = ctx.asignacion().ID().getText()
            valor= self.obtenerValor(ctx.asignacion().opal())
            print(asignacion +" = " + f" {valor}")
            self.agregarCodigo(f"{asignacion} = {valor}")

        self.agregarCodigo(f"{etiqueta_inicio}:")
        
        if ctx.opal():
            condicion = self.procesarOpal(ctx.opal())
            print(f"Condición: {condicion}")
            self.agregarCodigo(f"if NOT ({condicion}) goto {etiqueta_salida}")
        
        print("Cuerpo del For:")
        
        if ctx.bloque():
            self.visitBloque(ctx.bloque())
        else:
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if hasattr(child, 'getRuleIndex') and isinstance(child, compiladoresParser.InstruccionContext):
                    self.visit(child)
        
       
        if ctx.paramFor():
            if ctx.paramFor().incremento():
                var_inc = ctx.paramFor().incremento().ID().getText()
                self.agregarCodigo(f"{var_inc} = {var_inc} + 1")
            elif ctx.paramFor().decremento():
                var_dec = ctx.paramFor().decremento().ID().getText()
                self.agregarCodigo(f"{var_dec} = {var_dec} - 1")
            elif ctx.paramFor().asignacion():
                asig = ctx.paramFor().asignacion().ID().getText()
                valor_asig = self.procesarOpal(ctx.paramFor().asignacion().opal())
                self.agregarCodigo(f"{asig} = {valor_asig}")

        self.agregarCodigo(f"goto {etiqueta_inicio}")
 
        self.agregarCodigo(f"{etiqueta_salida}:")
        
        print("=-"*20)


    def visitAsignacion(self, ctx:compiladoresParser.AsignacionContext):
        print("=-"*20)
        print("SE ENCONTRO UNA ASIGNACION")
        print("=-"*20)
        variable = ctx.ID().getText()
        if ctx.opal():
           
            valor = self.procesarOpal(ctx.opal())
            print(variable +" = " + f" {valor}")
            
         
            self.agregarCodigo(f"{variable} = {valor}")
            
        elif ctx.char():
      
            char_valor = ctx.char().getText()
            print(variable +" = " + f" {char_valor}")
      
            self.agregarCodigo(f"{variable} = {char_valor}")
            
        print("=-"*20)



    #Parte de las opal con expreciones
    #--------------------------------------------------------------------------------
    def procesarOpal(self, ctx:compiladoresParser.OpalContext):
        
        if ctx.exp():
            return self.procesarExp(ctx.exp())
        elif ctx.oplo():
            return self.procesarOplo(ctx.oplo())
        elif ctx.callFunc():
            return self.procesarCallFunc(ctx.callFunc())


    def procesarExp(self, ctx:compiladoresParser.ExpContext):
    
        resultado = self.procesarTerm(ctx.term())
        
        # Procesar la cadena de sumas/restas
        if ctx.e():
            resultado = self.procesarE(ctx.e(), resultado)
        
        return resultado

    def procesarE(self, ctx:compiladoresParser.EContext, izquierda):
    
        while ctx is not None and ctx.term() is not None:
            operador = "+" if ctx.SUMA() else "-"
            derecha = self.procesarTerm(ctx.term())
            
            # Generar temporal para la operación binaria
            temporal = self.generarTemporal()
            self.agregarCodigo(f"{temporal} = {izquierda} {operador} {derecha}")
            
            izquierda = temporal
            
            # Procesar el siguiente nivel
            if ctx.e():
                ctx = ctx.e()
            else:
                ctx = None
        
        return izquierda

    def procesarTerm(self, ctx:compiladoresParser.TermContext):

        resultado = self.procesarFactor(ctx.factor())
        
        # Procesar la cadena de mult/div/mod
        if ctx.t():
            resultado = self.procesarT(ctx.t(), resultado)
        
        return resultado

    def procesarT(self, ctx:compiladoresParser.TContext, izquierda):

        while ctx is not None and ctx.factor() is not None:
            if ctx.MULT():
                operador = "*"
            elif ctx.DIV():
                operador = "/"
            elif ctx.MOD():
                operador = "%"
            else:
                operador = "*"
            
            derecha = self.procesarFactor(ctx.factor())
            
            temporal = self.generarTemporal()
            self.agregarCodigo(f"{temporal} = {izquierda} {operador} {derecha}")
            
            izquierda = temporal
            

            if ctx.t():
                ctx = ctx.t()
            else:
                ctx = None
        
        return izquierda

    def procesarFactor(self, ctx:compiladoresParser.FactorContext):
        if ctx.NUMERO():
            return ctx.NUMERO().getText()
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.exp():
            return self.procesarExp(ctx.exp())
        return ctx.getText()
    #--------------------------------------------------------------------------------
    
    #Parte de las OPLO
    #--------------------------------------------------------------------------------
    def procesarOplo(self, ctx: compiladoresParser.OploContext):
        izquierda = self.procesarAnd(ctx.and_())
        return self.procesarOr(ctx.or_(), izquierda)
    
    def procesarOr(self, ctx, izquierda):
        while ctx is not None and ctx.and_() is not None:
            derecha = self.procesarAnd(ctx.and_())

            t = self.generarTemporal()
            self.agregarCodigo(f"{t} = {izquierda} || {derecha}")
            izquierda = t

            ctx = ctx.or_()

        return izquierda


    def procesarAnd(self, ctx: compiladoresParser.AndContext):
        izquierda = self.procesarCmp(ctx.cmp())
        return self.procesarA(ctx.a(), izquierda)

    def procesarA(self, ctx: compiladoresParser.AContext, izquierda):
        while ctx is not None and ctx.cmp() is not None:
            derecha = self.procesarCmp(ctx.cmp())

            t = self.generarTemporal()
            self.agregarCodigo(f"{t} = {izquierda} && {derecha}")
            izquierda = t

            ctx = ctx.a() if ctx.a() else None

        return izquierda

    def procesarCmp(self, ctx: compiladoresParser.CmpContext):
        izquierda = self.procesarExp(ctx.exp())
        return self.procesarC(ctx.c(), izquierda)
    
    def procesarC(self, ctx: compiladoresParser.CContext, izquierda):
        if ctx is None:
            return izquierda

        operador = ctx.getChild(0).getText()  # == != < > <= >=
        derecha = self.procesarExp(ctx.exp())

        t = self.generarTemporal()
        self.agregarCodigo(f"{t} = {izquierda} {operador} {derecha}")
        return t

    #--------------------------------------------------------------------------------

    def procesarCallFunc(self, ctx: compiladoresParser.CallFuncContext):

        nombre = ctx.ID().getText()
        cantidad = 0

        # Procesar parámetros si existen
        if ctx.var():
            for expr in ctx.var().exp():
                valor = self.procesarExp(expr)
                self.agregarCodigo(f"push {valor}")
                cantidad += 1

        # Generar temporal para el retorno
        temp = self.generarTemporal()
        self.agregarCodigo(f"{temp} = call {nombre}")

        return temp


    def obtenerValor(self, ctx):
        return ctx.getText()

    def generarTemporal(self):
        self.temporales += 1
        return f"t{self.temporales}"

    def generarEtiqueta(self):
        self.etiquetas += 1
        return f"L{self.etiquetas}"

    def visitIncremento(self, ctx:compiladoresParser.IncrementoContext):
        print("=-"*20)
        print("SE ENCONTRO UN INCREMENTO")
        print("=-"*20)
        var = ctx.ID().getText()
        print(f"{var}++")
        self.agregarCodigo(f"{var} = {var} + 1")
        print("=-"*20)

    def visitDecremento(self, ctx:compiladoresParser.DecrementoContext):
        print("=-"*20)
        print("SE ENCONTRO UN DECREMENTO")
        print("=-"*20)
        var = ctx.ID().getText()
        print(f"{var}--")
        self.agregarCodigo(f"{var} = {var} - 1")
        print("=-"*20)

    def visitReturn(self, ctx:compiladoresParser.ReturnContext):
        print("=-"*20)
        print("SE ENCONTRO UN RETURN")
        print("=-"*20)
        if ctx.opal():
            valor = self.obtenerValor(ctx.opal())
            print(f"return {valor}")
            self.agregarCodigo(f"return {valor}")
        else:
            print("return")
            self.agregarCodigo(f"return")
        print("=-"*20)

    def visitFunc(self, ctx:compiladoresParser.FuncContext):
        print("=-"*20)
        print("SE ENCONTRO UNA DEFINICION DE FUNCION")
        print("=-"*20)
        tipo = ctx.getChild(0).getText()
        nombre = ctx.ID().getText()
        argumentos = [] #Esta es la lista de argumentos de las funcoines
        print(f"Función: {tipo} {nombre}()")
        self.agregarCodigo(f"function {nombre}():")
        
        #Entramos a ver los argumentos
        if ctx.var_func():
            argfunc = ctx.var_func()


            for i in range(argfunc.getChildCount()):
                pf = argfunc.getChild(i)
        
                if hasattr(pf, 'getSymbol') and pf.getSymbol().type == compiladoresParser.ID:
                    argumentos.append(pf.getText())



        for j in reversed(argumentos):
            self.agregarCodigo(f"pop {j}")

        if ctx.bloque():
            self.visitBloque(ctx.bloque())
        print("=-"*20)

    def visitCallFunc(self, ctx: compiladoresParser.CallFuncContext):

        print("=-"*20)
        print("SE ENCONTRO UNA LLAMADA A FUNCION")
        print("=-"*20)

        nombre = ctx.ID().getText()
        cantidad = 0

        if ctx.var():
            for expr in ctx.var().exp():
                valor = self.procesarExp(expr)
                self.agregarCodigo(f"push {valor}")
                cantidad += 1

        self.agregarCodigo(f"call {nombre}")

        print("=-"*20)


    def visitProto(self, ctx:compiladoresParser.ProtoContext):
        print("=-"*20)
        print("SE ENCONTRO UN PROTOTIPO")
        print("=-"*20)
        tipo = ctx.getChild(0).getText()
        nombre = ctx.ID().getText()
        print(f"Prototipo: {tipo} {nombre}()")
        self.agregarCodigo(f"proto {tipo} {nombre}()")
        print("=-"*20)

    def agregarCodigo(self, instruccion):
        self.codigo_intermedio.append(instruccion)

    def mostrarCodigoIntermedio(self):
        print("\n" + "="*50)
        print("CÓDIGO DE 3 DIRECCIONES")
        print("="*50)
        for i, instruccion in enumerate(self.codigo_intermedio, 1):
            print(f"{i:3d}. {instruccion}")
        print("="*50 + "\n")
        

        self.guardarCodigoIntermedio()

    def guardarCodigoIntermedio(self):

        archivo = "src/main/python/dhs/output/codigo_intermedio.txt"
        try:
            with open(archivo, 'w', encoding='utf-8') as f:
                for i, instruccion in enumerate(self.codigo_intermedio, 1):
                    f.write(f"{i:3d}. {instruccion}\n")
            print(f"Código de 3 direcciones guardado en: {archivo}")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")