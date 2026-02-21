import sys
from antlr4 import *
from compiladoresLexer import compiladoresLexer
from compiladoresParser import compiladoresParser
from Escucha import Escucha
from Walker import Walker
from Optimizador import Optimizador


def main(argv):
    #archivo = "DHS/input/opal.txt"
    archivo = "input/opal.txt"

    if len(argv) > 1 :
        archivo = argv[1]
    input = FileStream(archivo)
    lexer = compiladoresLexer(input)
    stream = CommonTokenStream(lexer)
    parser = compiladoresParser(stream)
    escucha = Escucha()
    parser.addParseListener(escucha)
    tree = parser.programa()
    #if escucha.hubo_error:
    #    print("\n[!] La compilación falló debido a errores semánticos. No se generará código.")
    #    return
    #print(tree.toStringTree(recog=parser))
    caminante = Walker()
    caminante.visitPrograma(tree)
    Optimizador.iniciarOptimizacion(
       "src/main/python/dhs/output/codigo_intermedio.txt", "src/main/python/dhs/output/codigo_optimizado.txt"
    )
    #Agregar una lista de declaracion
    #Podemos asignar el valor al momento de declarar la variable.
    #implementamos el visitor que genera codigo intermedio 

if __name__ == '__main__':
    main(sys.argv)