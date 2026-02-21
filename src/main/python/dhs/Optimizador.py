import re
from util.Constante import Constante

class Optimizador:
    @staticmethod
    
    # --- FASE DE ANÁLISIS: Conteo de uso de variables ---
    # Sirve para identificar qué variables son necesarias y cuáles pueden ser eliminadas
    # si no se usan más adelante (especialmente variables temporales 't').
    
    def contarUsos(lineas):
        usos = {}
        print("\n--- Contando usos de variables ---\n")
        for linea in lineas:
            texto = re.sub(r'^\s*\d+\.\s*', '', linea) # Elimina el número de línea al inicio (ej. "1. ") para analizar solo el código
            m = Constante.asignacion.match(texto) # Solo analizamos las asignaciones para contar usos, ya que en otras líneas (como if o return) no definimos variables, solo las usamos.
            if m: texto = m.group(2) # Solo analizamos la expresión a la derecha del '=' para contar usos, no la variable que se define a la izquierda
            for v in Constante.usoVariable.findall(texto): # Busca todas las variables usadas en la línea (ej. x, y, t1) y cuenta su uso
                usos[v] = usos.get(v, 0) + 1 # Incrementa el conteo de uso para cada variable encontrada
        print("\n--- Conteo de usos completado ---\n")
        return usos

    @classmethod
    # --- FASE 1: Optimización Local y Propagación ---
    def optimizar(cls, lineas_codigo):
        print("\n--- Iniciando optimización ---\n")
        codigo = []
        tabla = {} # Diccionario para rastrear valores constantes (Propagación de constantes)
        usos = cls.contarUsos(lineas_codigo)
        etiquetas_vistas = set()

        for linea in lineas_codigo:
            
            # Limpiar número de línea
            instr = re.sub(r'^\s*\d+\.\s*', '', linea).strip()
            if not instr: 
                continue
            
            # CONTROL DE FLUJO: Si entramos a una función o etiqueta, el contexto cambia.
            # Se limpia la tabla para evitar propagar valores de un bloque a otro de forma errónea.
            if Constante.nombreFuncion.match(instr) or Constante.etiqueta.match(instr):
                print(f"Entrando a función/etiqueta: {instr}, limpiando contexto.")
                tabla.clear()
                etiquetas_vistas.clear()
                codigo.append(instr)
                continue
            
            # CONTROL DE FLUJO: Si hay un salto, los valores de las variables podrían cambiar 
            if instr.startswith("goto"):
                print(f"Encontrado salto: {instr}")
                destino = instr.split()[1]
                if destino in etiquetas_vistas: tabla.clear()
                print(f" Ciclo de salto a {destino}, limpiando contexto.")
                codigo.append(instr)
                continue
            if instr.startswith("push"):
                val_push = instr.replace("push", "").strip()
                # Propagar constantes (ej: t22 -> 3)
                for v, val in tabla.items():
                    val_push = re.sub(rf'\b{v}\b', str(val), val_push)
                codigo.append(f"push {val_push}")
                print(f"Optimización de PUSH: push {val_push}")
                continue

            # --- NUEVO: OPTIMIZACIÓN DE CALL (para argumentos) ---
            if "call" in instr:
                # Si el call es t23 = call ..., propagamos en el resto
                for v, val in tabla.items():
                    instr = re.sub(rf'\b{v}\b', str(val), instr)
                codigo.append(instr)
                continue
            
            # MANEJO DE ASIGNACIONES (EJ: x = a + b)
            m = Constante.asignacion.match(instr)
            if m:
                print(f"Optimización de asignación detectada: {instr}") # Ejemplo: x = a + b
                var = m.group(1).strip() # Variable que se asigna (ej. x)
                exp = m.group(2).strip() # Expresión que se asigna (ej. a + b)

                # PROPAGACIÓN: Sustituye variables por sus valores constantes conocidos
                for v, val in tabla.items(): #
                    exp = re.sub(rf'\b{v}\b', str(val), exp) # ej x -> 5, y -> 10 en la expresión x + y -> 5 + 10
                    
                # REDUCCIÓN DE POTENCIA E IDENTIDADES: Simplifica operaciones inútiles
                exp = re.sub(r'\b(\w+)\s*[\+\-]\s*0\b', r'\1', exp) # x + 0 -> x, x - 0 -> x
                exp = re.sub(r'\b0\s*\+\s*(\w+)\b', r'\1', exp) # 0 + x -> x
                exp = re.sub(r'\b(\w+)\s*[\*/]\s*1\b', r'\1', exp) # x * 1 -> x, x / 1 -> x
                exp = re.sub(r'\b1\s*\*\s*(\w+)\b', r'\1', exp) # 1 * x -> x
                exp = re.sub(r'\b(\w+)\s*\*\s*0\b', '0', exp) # x * 0 -> 0
                
                # PLEGAMIENTO DE CONSTANTES (Constant Folding): 
                # Si la expresión es puramente numérica (ej: 5 + 10), la resuelve.
                if re.fullmatch(r'^\s*\d+(\.\d+)?\s*[+\-*/%]\s*\d+(\.\d+)?\s*$', exp):
                    try:
                        print(f"Evaluando expresión constante: {exp}")
                        res = eval(exp) # Evaluar la expresión numérica
                        print(f"Resultado de evaluación: {res}")
                        exp = str(int(res)) if isinstance(res, float) and res.is_integer() else str(res) # Convertir a entero si es un float sin parte decimal
                        print(f"Evaluando expresión constante: {exp}")
                    except: 
                        print(f"Error al evaluar expresión: {exp}")
                        pass

                # ELIMINACIÓN DE TEMPORALES NO USADOS:
                # Si es un temporal (t1) que se usa 1 o 0 veces, lo guardamos en tabla 
                # y no escribimos la línea para limpiar el código final.
                if var.startswith("t") and usos.get(var, 0) <= 1: # Solo consideramos temporales con 1 o 0 usos para eliminar
                    tabla[var] = exp
                    # Si es constante pura, no escribimos la línea
                    if re.fullmatch(r'[+-]?\d+(\.\d+)?', exp):  # Si la expresión resultante es un número, lo guardamos como constante pero no lo escribimos
                        print(f"Eliminando asignación a temporal no usado: {var} = {exp}")
                        continue

                # Actualizar la tabla de constantes si el resultado es un número
                if re.fullmatch(r'[+-]?\d+(\.\d+)?', exp): # Si la expresión resultante es un número, lo guardamos como constante
                    tabla[var] = exp
                else:
                    # Si ya no es constante, se quita de la tabla
                    tabla.pop(var, None)

                codigo.append(f"{var} = {exp}")
                print(f"Optimizando Final: {var} = {exp}")
                continue

            # OPTIMIZACIÓN DE IF: Propaga constantes dentro de la condición
            m_if = Constante.ifNot.match(instr)
            if  m_if: # Si es un if NOT, intentamos optimizar la condición
                cond, label = m_if.groups()
                # Intentamos propagar lo que ya sabemos
                for v, val in tabla.items(): # Reemplaza variables por sus valores constantes conocidos en la condición
                    cond = re.sub(rf'\b{v}\b', str(val), cond) # ej x -> 5, y -> 10 en la condición x > y -> 5 > 10
    
                    # Si la condición es constante (ej: 1 > 0), simplificamos el flujo
                    if re.fullmatch(r'[0-9+\-*/().\s%<>=!&|]+', cond): # Si la condición es puramente numérica, la evaluamos
                        try:
                            res = eval(cond.replace("&&", " and ").replace("||", " or ")) # Evaluar la condición lógica (reemplazando operadores lógicos para eval)
                            if not res: # El 'if NOT' salta si la condición es falsa
                                codigo.append(f"goto {label}") # Si res es False, el salto siempre ocurre, lo dejamos como goto
                                # Si res es True, el salto nunca ocurre, simplemente ignoramos la línea
                                continue
                        except: pass

                codigo.append(f"if NOT ({cond}) goto {label}")
                continue

            # OPTIMIZACIÓN DE RETURN: Propaga constantes en el retorno
            if instr.startswith("return"):
                ret = instr.replace("return", "").strip() # Extrae lo que se retorna
                for v, val in tabla.items(): # Reemplaza variables por sus valores constantes conocidos en el retorno
                    ret = re.sub(rf'\b{v}\b', str(val), ret) # ej x -> 5, y -> 10 en el retorno return x + y -> return 5 + 10
                codigo.append(f"return {ret}")
                print(f"Manteniendo RETURN optimizado: return {ret}")
                continue

            codigo.append(instr)
        print("\n --- Optimización completa ---")
        return codigo

# ---------------------------------------------------------------
    @classmethod
    def eliminarAsignacionesMuertas(cls, lineas):
        print("\n--- Ejecutando Limpieza de Código Muerto ---")
        
        # 1. Identificar qué variables se usan en condiciones o retornos
        siempre_vivas = set()
        for linea in lineas:
            if "if" in linea or "return" in linea:
                for v in Constante.usoVariable.findall(linea):
                    print(f"Variable '{v}' marcada como siempre viva por uso en: {linea.strip()}")
                    siempre_vivas.add(v)
    
        codigo_limpio = []
        variables_vivas = siempre_vivas.copy()
    
        # 2. Análisis reverso
        for linea in reversed(lineas):
            instr = re.sub(r'^\s*\d+\.\s*', '', linea).strip() # Limpiar número de línea
            if not instr: continue

            if instr.startswith("pop"):
                var_pop = instr.replace("pop", "").strip()
                variables_vivas.add(var_pop) # La variable que recibe el pop ahora está viva
                codigo_limpio.append(instr)
                continue
            # --- LA CLAVE PARA LOS IF/GOTOS ---
            # Si vemos una etiqueta, significa que un GOTO puede venir de cualquier parte.
            # Por seguridad, "resucitamos" las variables que sabemos que son importantes.
            if ":" in instr:
                for v in siempre_vivas:
                    print(f"Resucitando variable '{v}' por etiqueta: {instr}")
                    variables_vivas.add(v)
                codigo_limpio.append(instr)
                continue

            m = Constante.asignacion.match(instr)
            if m:
                var = m.group(1).strip()
                exp = m.group(2).strip()
            
                # Solo borramos si NO es una función y la variable NO está viva
                if var not in variables_vivas and "(" not in exp:
                    print(f"  Eliminando redundancia: {instr}")
                    continue
                
                # Si se queda, actualizamos variables vivas
                # 'var' sale porque aquí se define, las de 'exp' entran porque se usan
                variables_vivas.discard(var) # 
                for v in Constante.usoVariable.findall(exp):
                    print(f"  Variable '{v}' se mantiene viva por uso en: {instr}")
                    variables_vivas.add(v)
                codigo_limpio.append(instr)
            else:
                # Si es un goto o función, sus variables están vivas
                for v in Constante.usoVariable.findall(instr):
                    print(f"  Variable '{v}' se mantiene viva por uso en: {instr}")
                    variables_vivas.add(v)
                codigo_limpio.append(instr)
            
        return list(reversed(codigo_limpio))
# ---------------------------------------------------------------

    @classmethod
    def limpiarEtiquetas(cls, lineas):
        print("\n--- Iniciando limpieza y colapso de etiquetas ---")
        
        # 1. Mapeo de etiquetas consecutivas (Label Collapsing)
        # Si tenemos L7:\nL8:\nL6:, todas las referencias a L7 y L8 deben ir a L6
        mapa_alias = {}
        for i in range(len(lineas) - 1):
            act = lineas[i].strip()
            sig = lineas[i+1].strip()
            
            m_act = re.match(r'^(\w+):$', act) # Busca etiquetas en la línea actual
            m_sig = re.match(r'^(\w+):$', sig) # Busca etiquetas en la siguiente línea
            
            if m_act and m_sig: # Si la actual y la siguiente son etiquetas, colapsamos la actual hacia la siguiente
                orig = m_act.group(1)
                dest = m_sig.group(1)
                # Si el destino ya es un alias, seguimos la cadena
                mapa_alias[orig] = mapa_alias.get(dest, dest)
                print(f"  Colapsando: {orig} -> {mapa_alias[orig]}")

        # 2. Aplicar redirección de saltos y filtrar etiquetas
        # Primero necesitamos saber qué etiquetas quedan "vivas" tras el colapso
        lineas_intermedias = []
        for l in lineas:
            nueva_l = l
            # Redirigir todos los gotos a la etiqueta final del grupo
            for vieja, nuevo in mapa_alias.items():
                nueva_l = re.sub(rf'\bgoto\s+{vieja}\b', f"goto {nuevo}", nueva_l)
            
            # Solo mantenemos la línea si no es una etiqueta que fue colapsada hacia otra
            m_l = re.match(r'^(\w+):$', nueva_l.strip())
            if m_l and m_l.group(1) in mapa_alias:
                continue
            lineas_intermedias.append(nueva_l)

        # 3. Eliminar etiquetas huérfanas (que no tienen ningún goto apuntándoles)
        texto_final = "\n".join(lineas_intermedias) #
        lineas_finales = []
        for l in lineas_intermedias:
            m_e = re.match(r'^(\w+):$', l.strip())
            if m_e:
                etiqueta = m_e.group(1)
                # Buscamos si alguien salta a esta etiqueta
                if re.search(rf'goto\s+{etiqueta}\b', texto_final):
                    lineas_finales.append(l)
                else:
                    print(f"  Borrando etiqueta huérfana: {etiqueta}")
            else:
                lineas_finales.append(l)

        return lineas_finales


    @classmethod
    def iniciarOptimizacion(cls, archivo_entrada, archivo_salida):
        with open(archivo_entrada, 'r', encoding='utf-8') as f:
            resultado = f.readlines()

        for _ in range(7):
            print(f"\n--- Iteración de optimización {_ + 1} ---\n")
            resultado = cls.optimizar(resultado)
            resultado = cls.eliminarAsignacionesMuertas(resultado)
            resultado = cls.limpiarEtiquetas(resultado)
        

        with open(archivo_salida, 'w', encoding='utf-8') as f:
            for i, linea in enumerate(resultado, 1):
                f.write(f"{i:3d}. {linea}\n")
        print("\n---Optimización finalizada con éxito ---\n")