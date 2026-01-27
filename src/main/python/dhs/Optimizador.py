from util.ManejadorArchivos import ManejadorArchivos
from util.Constante import Constante
import re

class Optimizador:
    
    temporales = {}
    enPila = []
    tmpF = {}
    
    pasadas = 2
    
    funcion = False
    
    @staticmethod
    def optimizar(linea, index = 0):
        with ManejadorArchivos(f'DHS/output/optimizacion_{index}.txt') as codIntermedio:
            linea = ManejadorArchivos.sacarSaltosLinea(linea)
            lineaTmp = linea
            linea = ManejadorArchivos.sacarEspacios(linea)
            if Constante.etiqueta.match(linea) or linea.startswith('jmp') or ManejadorArchivos.sacarEspacios(linea) == 'endmain' or linea.startswith('label'): 
                codIntermedio.write(lineaTmp + '\n')
                
            elif Constante.pilaPush.match(linea):
                match = re.match(Constante.PushPop, linea)
                tmp = [match.group(1), match.group(2)]
                if tmp[1] in Optimizador.temporales:
                    codIntermedio.write(f'{tmp[0]} {Optimizador.temporales[tmp[1]]}\n')
                else:
                    codIntermedio.write(lineaTmp + '\n')

            elif Constante.asignacion.match(linea) and linea.find('t') < 0:
                tmp = linea.split('=')
                if Constante.variables.match(tmp[1]) and tmp[1] in Optimizador.temporales:
                    codIntermedio.write('\n' + f'{tmp[0]} = {codIntermedio.temporales[tmp[1]]}')
                Optimizador.temporales[tmp[0]] = tmp[1]
                
            elif Constante.tmpNumeroLetra.match(linea) and not (any(simbolo in linea for simbolo in Constante.listSimbolos)):
                tmp = linea.split('=')
                Optimizador.temporales[tmp[0]] = tmp[1]
                
            elif Constante.tmpLetra.match(linea):
                tmp =linea.split('=')
                if tmp[1] in Optimizador.temporales:
                    temp2 = Optimizador.temporales[tmp[1]]
                    codIntermedio.write(f'{tmp[0]} = {temp2}\n')
                else:
                    codIntermedio.write(f'{tmp[0]} = {tmp[1]}' + '\n')
            
            elif Constante.opal.match(linea) and any(simbolo in linea for simbolo in Constante.listSimbolos):
                tmp = linea.split('=')
                simbolo = re.findall(Constante.simbolos, linea)
                elementos = re.split(Constante.simbolos,tmp[1])
                # verifica su los 2 terminos son enteros para sumarlos
                if bool(Constante.entero.match(elementos[0])) == True and bool(Constante.entero.match(elementos[1])) == True:
                   codIntermedio.write(f'\n{tmp[0]} {simbolo[0]} {eval(tmp[1])}')
                else:
                    # verifica su los 2 terminos son decimales para sumarlos
                    if bool(Constante.decimal.match(elementos[0])) == True and bool(Constante.decimal.match(elementos[1])) == True:
                       tmp2 = float(elementos[0]) + float(elementos[1])
                       codIntermedio.write(f'\n{tmp[0]} {simbolo[0]} {tmp[1]}')
                    else:
                        if bool(Constante.tmp.match(elementos[0])):
                            if elementos[0] in Optimizador.temporales:
                               codIntermedio.write(
                                    '\n' + f'{tmp[0]} {simbolo[0]} {Optimizador.temporales[elementos[0]]}')
                            else:
                               codIntermedio.write(
                                    '\n' + f'{tmp[0]} {simbolo[0]} {elementos[0]}')
                        else:
                           codIntermedio.write(
                                '\n' + f'{tmp[0]} {simbolo[0]} {elementos[0]}')
                        if elementos[1] in Optimizador.temporales:
                            if elementos[1] in Optimizador.temporales:
                               tmp2 = Optimizador.temporales[elementos[1]]
                               codIntermedio.write(f' {simbolo[1]} {tmp2}')
                        else:
                            # temporales[tmp[0]] =tmp[1]
                            codIntermedio.write(f' {simbolo[1]} {elementos[1]}')
            elif Constante.ifNot.match(lineaTmp):
                # se obtiene el argumento del ifnot tmp[0] y del jmp tmp[1]
                tmp = re.findall(Constante.ifNotDivision, linea)
                tmp2 = [match for match in tmp[0]]
                if tmp2[0] in Optimizador.temporales:
                    codIntermedio.write(f'\nifnot {Optimizador.temporales[tmp2[0]]}')
                else:
                    codIntermedio.write(f'\nifnot {tmp2[0]}')
                if tmp2[1] in Optimizador.temporales:
                    codIntermedio.write(f' jmp {Optimizador.temporales[tmp2[1]]}')
                else:
                    codIntermedio.write(f' jmp {tmp2[1]}')
    
    
    @staticmethod
    def OptimizadorFuncion(linea, index = 0):
        with ManejadorArchivos(f'DHS/output/optimizacion_{index}.txt') as codIntermedio:
            linea = ManejadorArchivos.sacarSaltosLinea(linea)
            lineaTmp = linea
            linea = ManejadorArchivos.sacarEspacios(linea)
            if Constante.etiqueta.match(linea) or Constante.jmpFuncion.match(linea) or linea.startswith('label') or Constante.variableNumero.match(linea):
                codIntermedio.write(f'\n{lineaTmp}')

            elif Constante.pilaPop.match(linea):
                codIntermedio.write(f'\n{lineaTmp}')
                tmp = re.findall(Constante.pilaPop, linea)
                Optimizador.enPila.append(tmp[0])

            elif Constante.pilaPush.match(linea) and not any(simbolo in linea for simbolo in Constante.listSimbolos):
                match = (Constante.PushPop, linea)
                tmp = [match.group(1), match.group(2)]
                if tmp[1] in Optimizador.tmpF:
                    codIntermedio.write(f'\n{tmp[0]} {Optimizador.tmpF[tmp[1]]}')
                else:
                    codIntermedio.write(f'\n{lineaTmp}')

            elif linea.startswith('push'):
                codIntermedio.write(f'\n{lineaTmp}')

            # se guardan los tn = (numero o letra) en un diccionario
            # tn = numero o tn = letra o tn = booleano
            elif Constante.tmpNumeroLetra.match(linea) and not (any(simbolo in linea for simbolo in Constante.listSimbolos)) or Constante.opalLetas.match(linea):
                tmp = linea.split('=')
                Optimizador.tmpF[tmp[0]] = tmp[1]

            elif Constante.tmpLetra.match(linea):
                tmp = linea.split('=')
                if tmp[1] in Optimizador.tmpF:
                    tmp2 = Optimizador.tmpF[tmp[1]]
                    codIntermedio.write('\n' + f'{tmp[0]} = {tmp2}')
                else:
                    codIntermedio.write('\n' + f'{tmp[0]} = {tmp[1]}')

            elif Constante.opal.match(linea) and any(simbolo in linea for simbolo in Constante.listSimbolos):
                tmp = linea.split('=')
                simbolo = re.findall(Constante.simbolos, linea)
                elementos = re.split(Constante.simbolos, tmp[1])

                if bool(Constante.entero.match(elementos[0])) == True and bool(Constante.entero.match(elementos[1])) == True:
                    codIntermedio.write(f'\n{tmp[0]} {simbolo[0]} {eval(tmp[1])}')
                else:
                    # verifica su los 2 terminos son decimales para sumarlos
                    if bool(Constante.decimal.match(elementos[0])) == True and bool(Constante.decimal.match(elementos[1])) == True:
                        tmp1 = float(elementos[0]) + float(elementos[1])
                        codIntermedio.write(f'\n{tmp[0]} {simbolo[0]} {tmp[1]}')
                    else:
                        if bool(Constante.tmp.match(elementos[0])):
                            if elementos[0] in Optimizador.enPila:
                                codIntermedio.write(
                                    '\n' + f'{tmp[0]} {simbolo[0]} {elementos[0]}')
                            else:
                                if elementos[0] in Optimizador.tmpF:
                                    codIntermedio.write(
                                        '\n' + f'{tmp[0]} {simbolo[0]} {Optimizador.tmpF[elementos[0]]}')
                        else:
                            codIntermedio.write(
                                '\n' + f'{tmp[0]} {simbolo[0]} {elementos[0]}')
                        if elementos[1] in Optimizador.enPila:
                            # temporales[tmp[0]] = tmp[1]
                            codIntermedio.write(f' {simbolo[1]} {elementos[1]}')
                        else:
                            if elementos[1] in Optimizador.tmpF:
                                tmp1 = Optimizador.tmpF[elementos[1]]
                                codIntermedio.write(f' {simbolo[1]} {tmp1}')
    
    @staticmethod
    def iniciarOptimizacion():
        cantidad = list(range(0, Optimizador.pasadas))
        
        for i in cantidad:
            with ManejadorArchivos(f'DHS/output/optimizacion_{i}.txt') as archivo:
                archivo.truncate(0)
        
        sinOptimizar = open('DHS/output/codIntermedio.txt', 'r')
        
            
        for linea in sinOptimizar:
            if len(re.findall(Constante.nombreFuncion, linea)) != 0 or Optimizador.funcion:
                Optimizador.OptimizadorFuncion(linea)
                Optimizador.funcion = True
            else:
                Optimizador.optimizar(linea)
        sinOptimizar.close()


        for i in cantidad[1:]:
            Optimizador.funcion = False
            optimizado = open(
                f'DHS/output/codIntermedioOptimizado{i - 1}.txt', 'r')
            lineas = optimizado.readlines()
            optimizado.close()
            for linea in lineas:

                if len(re.findall(Constante.nombreFuncion, linea)) != 0 or Optimizador.funcion:
                    Optimizador.OptimizadorFuncion(linea, i)
                    Optimizador.funcion = True
                else:
                    Optimizador.optimizar(linea, i)
                
                    
                
                