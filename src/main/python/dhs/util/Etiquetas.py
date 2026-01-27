class Etiquetas:
    
    _funcion = dict()
    _contador = 0
    
    def next_etiqueta(self):
        etiqueta = f'l{Etiquetas._contador}'
        Etiquetas._contador += 1
        return etiqueta
    
    def etiqueta_funcion(self, identificador):
        for id in Etiquetas._funcion:
            if str(id) == str(identificador):
                return Etiquetas._funcion[id]
            
        list = []
        etiqueta1 = Etiquetas.next_etiqueta(self)
        etiqueta2 = Etiquetas.next_etiqueta(self)
    
        list.append(etiqueta1)
        list.append(etiqueta2)
    
        Etiquetas._funcion[identificador] = list
    
        return list
    
    