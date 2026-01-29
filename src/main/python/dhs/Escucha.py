from antlr4.tree.Tree import ErrorNode, TerminalNode
from compiladoresListener import compiladoresListener
from compiladoresParser import compiladoresParser
from TablaSimbolos import TablaSimbolos
from Contexto import Contexto
from Id import ID, TipoDato


class Escucha(compiladoresListener) :


    def __init__(self):
        # Creamos la instancia de la Tabla de Simbolos
        self.TablaSimbolos = TablaSimbolos()
        self.numTokens = 0
        self.numNode = 0   

    # Vemos el comienzo del programa
    # -----------------------------------------------------------
    def enterPrograma(self, ctx:compiladoresParser.ProgramaContext):
        print("Comienza la Compilacion")

    # Exit a parse tree produced by compiladoresParser#programa.
    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
        
        
        print("Fin de la compilacion")
        print("Se encontraron")
        print("\tNodos: "+str(self.numNode))
        print("\tTokens: "+str(self.numTokens))

        print( "*******Identificadores no Usados*******" )
        print (TablaSimbolos.buscarNoUsados(TablaSimbolos))
    # -----------------------------------------------------------

    #Cuando usamos un bloque, estoy probando con while 
    # -----------------------------------------------------------
    def enterBloque(self, ctx: compiladoresParser.BloqueContext):
        print("---> Encontre un BLOQUE")
        context = Contexto()
        self.TablaSimbolos.addContexto(context)
        
    def exitBloque(self, ctx: compiladoresParser.BloqueContext):
        
        print ("Salgo de un bloque")
        print ("Cantidad de hijos: " + str(ctx.getChildCount()))
        print("Tokens: " + str(ctx.getText()))

        print("Se encontro:")
        TablaSimbolos.contextos[-1].imprimirTabla()
        TablaSimbolos.delContexto(TablaSimbolos)


        return super().exitBloque(ctx)
    # -----------------------------------------------------------

    #Ecuchamos si viene un while entonces hacemos...
    # -----------------------------------------------------------       
    def enterIwhile(self, ctx: compiladoresParser.IwhileContext):
        return super().enterIwhile(ctx)
    
    def exitIwhile(self, ctx: compiladoresParser.IwhileContext):
        opal = ctx.opal()
        pa = ctx.PA()
        pc = ctx.PC()
        #Lo que tenemos que hacer aca es comprobar si tenemos ambos parentesis en el while 

        if pa == None :
            print( "ERROR, se espera un '(' " )
            return None

        if pc == None :
            print ( "ERROR, se espera un ')'" )
            return None
        
        if opal == None : 
            print ( "ERROR, se espera una operacion aritmetica o logica")
            return None
        #En el caso de tenerlos tenemos que comprobar si tenemos el opal.

        
        
        return super().exitIwhile(ctx)
    # -----------------------------------------------------------

    # Esto es para el if
    # -----------------------------------------------------------
    def enterIf(self, ctx: compiladoresParser.IfContext):
        return super().enterIf(ctx)
    
    def exitIf(self, ctx: compiladoresParser.IfContext):
        
        opal = ctx.opal()
        pa = ctx.PA()
        pc = ctx.PC()
        #Lo que tenemos que hacer aca es comprobar si tenemos ambos parentesis en el while 
        print ("Entra")
        if pa == None :
            print( "ERROR, se espera un '(' " )
            return None

        if pc == None :
            print ( "ERROR, se espera un ')'" )
            return None
        
        if opal == None : 
            print ( "ERROR, se espera una operacion aritmetica o logica")
        return super().exitIf(ctx)
    # -----------------------------------------------------------
    
    #Esto va a ser para el for, enrealidad tengo tener en cuenta mas cosas
    # -----------------------------------------------------------
    def enterIfor(self, ctx: compiladoresParser.IforContext):
        return super().enterIfor(ctx)
    
    def exitIfor(self, ctx: compiladoresParser.IforContext):
        
        opal = ctx.opal()
        pa = ctx.PA()
        pc = ctx.PC()
        asig = ctx.asignacion()

        #Lo que tenemos que hacer aca es comprobar si tenemos ambos parentesis en el while 
        
        if pa == None :
            print( "ERROR, se espera un '(' " )
            return None

        if pc == None :
            print ( "ERROR, se espera un ')'" )
            return None
        
        if opal == None : 
            print ( "ERROR, se espera una operacion aritmetica o logica")
            return None
        
        if asig == None :
            print( "ERROR, se espera una asignacion " )
            return None
        
        return super().exitIf(ctx)
        

        return super().exitIfor(ctx)
    # -----------------------------------------------------------

    #Aca declaramos cuando inicializamos las variables...
    # -----------------------------------------------------------

    def enterInit(self, ctx: compiladoresParser.InitContext):
        print ("---> Inicializamos una variable") 
        return super().enterInit(ctx)
    



    def exitInit(self, ctx: compiladoresParser.InitContext):
        
        tipoDato = ctx.getChild(0).getText()


        i = 1

        while i < ctx.getChildCount() :

            nombre = ctx.getChild(i).getText()

            comprobarGlobal = TablaSimbolos.buscarGlobal(TablaSimbolos, nombre)

            if comprobarGlobal == 1 :
                if TablaSimbolos.buscarLocal( TablaSimbolos, nombre) == 1:
                    print ("Se agrego correctamente la variable")
                    print ("--------------------------------------")
        
                    print("--->Tipo de dato: " + tipoDato)
                    print("--->Nombre de Variable: " + nombre ) 

                    print ("--------------------------------------")
        
                    TablaSimbolos.addIdentificador(TablaSimbolos, nombre, tipoDato)
                else: 
                    print ("---> El id ya esta en uso...")
            else :
               print ("---> El id ya esta en uso...")

            i = i + 2

        # comprobarGlobal = TablaSimbolos.buscarGlobal(TablaSimbolos, nombre)

        # if comprobarGlobal == 1 :

        #     if TablaSimbolos.buscarLocal( TablaSimbolos, nombre) == 1:
        #         print ("Se agrego correctamente la variable")
        #         print ("--------------------------------------")
        
        #         print("--->Tipo de dato: " + tipoDato)
        #         print("--->Nombre de Variable: " + nombre ) 

        #         print ("--------------------------------------")
        
        #         TablaSimbolos.addIdentificador(TablaSimbolos, nombre, tipoDato)
        #     else: 
        #         print ("---> El id ya esta en uso...")
        # else :
        #     print ("---> El id ya esta en uso...")

        return super().exitInit(ctx)
    # -----------------------------------------------------------
    

    #Esta parte la vamos a usar para las asignaciones.
    # -----------------------------------------------------------
    def enterAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        
        print("---> Se encontro una asignacion...")
        
        return super().enterAsignacion(ctx)
    
    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        nombre = ctx.getChild(0).getText()
        # Buscamos el ID de la variable destino
        identificador = self.TablaSimbolos.buscarLocal(nombre)
        if identificador == 1:
            identificador = self.TablaSimbolos.buscarGlobal(nombre)

        if identificador != 1:
            valor_ctx = ctx.getChild(2)
            valor_texto = valor_ctx.getText()
            
            # --- VALIDACIÓN DE TIPOS ---
            # 1. Evitar asignar un literal char (con '') a un int
            if identificador.tipoDato == TipoDato.INT and "'" in valor_texto:
                print(f"ERROR SEMANTICO: No se puede asignar CHAR a variable INT '{nombre}'")
                return

            # 2. Evitar sumar variables de tipo char en una expresion int
            # Recorremos los hijos de la expresion buscando IDs
            for i in range(valor_ctx.getChildCount()):
                token = valor_ctx.getChild(i)
                # Si el hijo es un ID (variable) en la suma/operacion
                if hasattr(token, 'ID') and token.ID():
                    var_expr = self.TablaSimbolos.buscarLocal(token.getText())
                    if var_expr == 1: var_expr = self.TablaSimbolos.buscarGlobal(token.getText())
                    
                    if var_expr != 1:
                        if identificador.tipoDato == TipoDato.INT and var_expr.tipoDato == TipoDato.CHAR:
                            print(f"ERROR SEMANTICO: No se puede sumar '{var_expr.nombre}' (char) en la variable '{nombre}' (int)")
                            return

            identificador.inicializado = 1
            print(f"Asignación válida: {nombre} = {valor_texto}")
        else:
            print(f"ERROR: Variable '{nombre}' no declarada.")

    # -----------------------------------------------------------
    # Exit a parse tree produced by compiladoresParser#programa.


    def exitPrograma(self, ctx:compiladoresParser.ProgramaContext):
         print("Nombre Variable: "+ ctx.getChild(1).getText())  
         
    def visitTerminal(self, node: TerminalNode):
        #print("----> Token: " + node.getText())
        self.numTokens =+ 1
        
    def visitErrorNode(self, node: ErrorNode):
        print("----> ERROR ")
        
    def enterEveryRule(self, ctx):
        self.numNode += 1

    #Aca se va a declarar las fuciones...
     # -----------------------------------------------------------
   
    def enterFunc(self, ctx: compiladoresParser.FuncContext):
        print("---> Se ingreso una funcion... ")
        
        return super().enterFunc(ctx)
    
    def exitFunc(self, ctx: compiladoresParser.FuncContext):
        

        #Primero compruebo que este bien escrita

        pa = ctx.PA()
        pc = ctx.PC()
        #Lo que tenemos que hacer aca es comprobar si tenemos ambos parentesis en el while 
        
        if pa == None :
            print( "ERROR, se espera un '(' " )
            return None

        if pc == None :
            print ( "ERROR, se espera un ')'" )
            return None
        
        retorno = ctx.getChild(0).getText()
        nombrefuncion = ctx.getChild(1).getText()

        buscarGlobal = TablaSimbolos.buscarGlobal(TablaSimbolos, nombrefuncion)

        comprobar = False
        listaParametros = []

        if buscarGlobal == 1:
            print ( "ERROR, la funcion no tiene declarado un prototipo" )
            return None;
        parametros = ctx.var_func()

        if parametros and parametros.getChildCount() > 0:
                
            comprobar = True

            i = 0
            while i < parametros.getChildCount() :
            
                tipo = parametros.getChild(i).getText()
                nombre = parametros. getChild(i+1).getText()
                listaParametros.append(f"{tipo} {nombre}")
                i+=3

            print ("---> La funcion ' " + nombrefuncion + " ' fue ingresada correctamente")
            print ("--------------------------------------")
            print ("Nombre: " + nombrefuncion)
            print ("Tipo de Retorno: " + retorno)
            
        if comprobar :
            print("Parametros: ")
            print(listaParametros)
        else :
            print("La funcion no necesita parametros")    
        print ("--------------------------------------")       

        
        

    #Aca declaramos el prototipo 
    # -----------------------------------------------------------
    def enterProto(self, ctx: compiladoresParser.ProtoContext):
        print ("---> Encontre un prototipo")
        return super().enterProto(ctx)
    
    def exitProto(self, ctx: compiladoresParser.ProtoContext):
        
        retorno = ctx.getChild(0).getText()
        nombrePrototipo = ctx.getChild(1).getText()
        
        #Lo primero que quiero comprobar es que este cuente con el punto y coma 


        buscarGlobal = TablaSimbolos.buscarGlobal(TablaSimbolos, nombrePrototipo)

        comprobar = False
        listaParametros = []

        if buscarGlobal == 1 :

            parametros = ctx.var_func()

            if parametros and parametros.getChildCount() > 0:
                
                comprobar = True

                i = 0

                while i < parametros.getChildCount() :
            
                    tipo = parametros.getChild(i).getText()
                    nombre = parametros. getChild(i+1).getText()
                    listaParametros.append(f"{tipo} {nombre}")

                    i+=3

            print ("---> La funcion ' " + nombrePrototipo + " ' fue ingresada correctamente")
            print ("--------------------------------------")
            print ("Nombre: " + nombrePrototipo)
            print ("Tipo de Retorno: " + retorno)
            
            if comprobar :
                print("Parametros: ")
                print(listaParametros)
            else :
                print("La funcion no necesita parametros")
            
            print ("--------------------------------------")       
            TablaSimbolos.addIdentificador(TablaSimbolos, nombrePrototipo, retorno )
        else :
            print("ERROR!!! La funcion ' " + nombrePrototipo + " ' ya existe")
            return None
        return super().exitProto(ctx)
    # -----------------------------------------------------------

    #Esta es la parte de las opal
    #------------------------------------------------------------------
    def enterFactor(self, ctx: compiladoresParser.FactorContext):
        
        return super().enterFactor(ctx)

    def exitFactor(self, ctx: compiladoresParser.FactorContext):
        
        nombreVariable = ctx.ID() #Aca lo que puede pasar es que no tengamos un id como factor, entonces devuelve none en ese caso

        if nombreVariable != None : 
            busqueda = TablaSimbolos.buscarLocal(TablaSimbolos, nombreVariable.getText()) #Aca lo que vamos a hacer es buscarlo dentro de la tabla de simbolos...
            #comprobamos is esta inicializada la variable
            if busqueda == 1:
                print( "ERROR, variable no existente" )
                return None
                
            if busqueda.inicializado == 1: 
                    #Vamos a definir la variable como usada

                    busqueda.usado = 1
            else :
                print("ERROR, la variable no a sido inicializada")
                return None
 
            if busqueda == 1:
                busqueda = TablaSimbolos.buscarGlobal(TablaSimbolos ,nombreVariable)

                if busqueda == 1:
                    print( "ERROR, variable no existente" )
                    return None
                
                #comprobamos si fue inicializada, si no fue asi no se conoce el valor, por lo que no podemos hacer nada con ella
                if busqueda.inicializado == 1: 
                    #Vamos a definir la variable como usada
                    busqueda.usado = 1 
                else :
                    print("ERROR, la variable no a sido inicializada")
                    

        return super().exitFactor(ctx)
    #Aca vamos a definir la llamadas a funciones...
    #------------------------------------------------------------------
    def enterCallFunc(self, ctx: compiladoresParser.CallFuncContext):
        return super().enterCallFunc(ctx)
    

    def exitCallFunc(self, ctx: compiladoresParser.CallFuncContext):
        
        nombre = ctx.getChild(0).getText()

        comprobarGlobal = TablaSimbolos.buscarGlobal(TablaSimbolos, nombre)

        if comprobarGlobal == 1 :

            print("ERROR, la funcion no esta definida")
            return None
        
        
        
        return super().exitCallFunc(ctx)
        #La parte de comprobar si las variables estan inicializadas ya esta echa, porque como sabemos podemos tener
        #funciones aritmeticas en las mismas, entonces son comprobadas por factor.
    #------------------------------------------------------------------


    #Parte de incremento y decremento 
    #------------------------------------------------------------------

    def enterIncremento(self, ctx: compiladoresParser.IncrementoContext):
        return super().enterIncremento(ctx)

    def exitIncremento(self, ctx: compiladoresParser.IncrementoContext):


        variable = ctx.getChild(0).getText()

        local = TablaSimbolos.buscarLocal(TablaSimbolos, variable)
        #Aca vamos a buscar si se encuentra declarada de manera local
        if local != 1:
            # si si

            #Comprobamos si la variable esta inicializada

            if local.inicializado != 1 : 
                print ( "ERROR, la variable no esta declarada" )
                return None
            
            # En el caso de si estar inicializada lo que vamos a hacer es ponerla como usada.

            local.usado = 1
        else :
            
            #Ahora la vamos a buscar pero globalmente
            glob = TablaSimbolos.buscarGlobal(TablaSimbolos, variable)

            if glob == 1:
                print ( "ERROR, la variable no esta declarada" )
                return None
            
            if glob.inicializado != 1 : 
                print ( "ERROR, la variable no esta inicializado" )
                return None
            

            #Si esta la encontramos 
            glob.usado = 1



        return super().exitIncremento(ctx)

    def enterDecremento(self, ctx: compiladoresParser.DecrementoContext):
        return super().enterDecremento(ctx)
    
    def exitDecremento(self, ctx: compiladoresParser.DecrementoContext):

        variable = ctx.getChild(0).getText()

        local = TablaSimbolos.buscarLocal(TablaSimbolos, variable)
        #Aca vamos a buscar si se encuentra declarada de manera local
        if local != 1:
            # si si

            #Comprobamos si la variable esta inicializada

            if local.inicializado != 1 : 
                print ( "ERROR, la variable no esta declarada" )
                return None
            
            # En el caso de si estar inicializada lo que vamos a hacer es ponerla como usada.

            local.usado = 1
        else :
            
            #Ahora la vamos a buscar pero globalmente
            glob = TablaSimbolos.buscarGlobal(TablaSimbolos, variable)

            if glob == 1:
                print ( "ERROR, la variable no esta declarada" )
                return None
            
            if glob.inicializado != 1 : 
                print ( "ERROR, la variable no esta inicializado" )
                return None
            

            #Si esta la encontramos 
            glob.usado = 1



        return super().exitDecremento(ctx)

    #------------------------------------------------------------------

    
    #Para comprobar si hace falta un punto y coma 
    #------------------------------------------------------------------
    def enterPuntoYComa(self, ctx: compiladoresParser.PuntoYComaContext):
        return super().enterPuntoYComa(ctx)
    
    def exitPuntoYComa(self, ctx: compiladoresParser.PuntoYComaContext):
        #Comprobamos si tenemos el punto y coma en nuestra instruccion
        puntoYComa = ctx.PYC()
        if puntoYComa == None:
            print ( "ERROR, se espera un: ';'" )
            return None;
     
        return super().exitPuntoYComa(ctx)
    #------------------------------------------------------------------
    
    def exitInit(self, ctx: compiladoresParser.InitContext):
        tipoDatoStr = ctx.getChild(0).getText()
        i = 1
        while i < ctx.getChildCount():
            nombre = ctx.getChild(i).getText()
            if nombre == ';': break
            
            # USAR self.TablaSimbolos (la instancia)
            if self.TablaSimbolos.buscarLocal(nombre) == 1:
                self.TablaSimbolos.addIdentificador(nombre, tipoDatoStr)
                print(f"---> Variable declarada: {tipoDatoStr} {nombre}")
            else:
                print(f"ERROR: El identificador '{nombre}' ya existe.")
            i += 2

    def exitAsignacion(self, ctx: compiladoresParser.AsignacionContext):
        nombre = ctx.getChild(0).getText()
        # Buscamos la variable en la Tabla de Símbolos
        identificador = self.TablaSimbolos.buscarLocal(nombre)
        if identificador == 1:
            identificador = self.TablaSimbolos.buscarGlobal(nombre)

        if identificador != 1:
            # Obtenemos el texto de lo que está a la derecha del '='
            valor_ctx = ctx.getChild(2)
            valor_texto = valor_ctx.getText()
            
            # Validación de tipos: evitar asignar char a int
            if identificador.tipoDato == TipoDato.INT:
                # Si el valor contiene una comilla simple, es un CHAR en tu gramática
                if "'" in valor_texto:
                    print(f"ERROR SEMANTICO: No se puede asignar el CHAR {valor_texto} a la variable INT '{nombre}'")
                    return
            
            identificador.inicializado = 1
            print(f"Asignación válida: {nombre} = {valor_texto}")
        else:
            print(f"ERROR: La variable '{nombre}' no ha sido declarada.")

    def exitFactor(self, ctx: compiladoresParser.FactorContext):
        if ctx.ID():
            nombre = ctx.ID().getText()
            busqueda = self.TablaSimbolos.buscarLocal(nombre)
            if busqueda == 1: busqueda = self.TablaSimbolos.buscarGlobal(nombre)
            
            if busqueda == 1:
                print(f"ERROR: Variable '{nombre}' no declarada.")
            elif busqueda.inicializado == 0:
                print(f"ERROR: Variable '{nombre}' no inicializada.")
            else:
                busqueda.usado = 1