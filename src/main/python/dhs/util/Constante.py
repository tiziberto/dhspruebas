# libreria usada para expresiones regulares
import re

class Constante:
    tmp = re.compile(r'\b(t\d+|[a-zA-Z])\b') 
    #/b se asegura que es una palabra completa
    booleano = re.compile(r'\b(?:True|False)\b', re.IGNORECASE)
    #re.IGNORECASE para que no distinga entre mayusculas y minusculas
    entero = re.compile(r'^[+-]?\d+$')
    #\d+ para uno o mas digitos
    decimal = re.compile(r'^[+-]?\d+\.\d+$')
    variables = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]*$')
    asignacion = re.compile(r'[a-zA-Z]+=\d+(\.\d+)?|[a-zA-Z]+=[a-zA-Z]+')
    etiqueta = re.compile(r'labell\d+|labelmain')
    pilaPush = re.compile(r'push\s+(t\d+|[a-zA-Z]|l\d+)')
    pilaPop = re.compile(r'pop\s*([a-zA-Z]|\bt\d+|l\d+)\b')
    jmpFuncion = re.compile(r'\bjmpl(?:[0-9]+|\w+)\b')
    #los dos siguiente son para identificar asignaciones de numeros o letras a temporales
    tmpNumeroLetra = re.compile(r't\d+=(\d+(\.\d+)?|[a-zA-Z])')
    tmpLetra = re.compile(r'[a-zA-Z]\s*=\s*t\d+\s*(?:\n|$)')
    opal = re.compile(
        r'\s*(?:[+\-*/%]|&&|\|\||[<>]=?|!=|==)\s*|\b(?:t\d+|[a-zA-Z]+|\d+(\.\d+)?)\b')
    opal2 = re.compile(
        r'\s*(?:[+\-*/%]|&&|\|\||[<>]=?|!=|==|t\d+)\s*|\b(?:t\d+|[a-zA-Z]+|\d+(\.\d+)?)\b')
    simbolos = r'[+\-*/%<>!=]|&&|\|\||=='
    listSimbolos = ['+', '-', '*', '/', '&&',
                     '||', '<=', '>=', '!=', '==', '%', '<', '>']
    ifNot = re.compile(r'\bifnot\b')
    ifNotDivision = re.compile(
        r'\bifnot\s*([a-zA-Z]+|\d+|True|False|t\d+)\s*jmp\s*([a-zA-Z]+|\d+|True|False|l\d+)\b', re.IGNORECASE)
    nombreFuncion = re.compile(r'label\s+((?!main|\bl\d+)\S+)')
    funcion = re.compile(r'\blabel\b\w*')
    # expresion para operaciones de letras y numeros asignados a temporales
    opalLetas = re.compile(r'\bt\d+[=][a-zA-Z]+\s*([+\-*/][a-zA-Z]+\s*)*\b')
    variableNumero = re.compile(r"^[a-zA-Z]=\d+$")
    PushPop = re.compile(r'^(push|pop)\s*(t\d+|[a-zA-Z]|l\d+|\d+)')

