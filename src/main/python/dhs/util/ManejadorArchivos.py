class ManejadorArchivos:
    
    def __init__(self, archivo):
        self.archivo = archivo
        
    def __enter__(self):
        self.archivo = open(self.archivo, 'a')
        return self.archivo
    
    def __exit__(self, tipo, excepcion, traza):
        if self.archivo:
            self.archivo.close()
            
    if __name__ == '__main__':
        with ManejadorArchivos('output/prueba.txt') as archivo:
            archivo.write('Hola, Mundo!\n')
            
            
    @staticmethod
    def sacarEspacios(datos):
        while (datos.find(' ') > 0):
            datos = datos.replace(' ', '')
        return datos
    
    @staticmethod
    def sacarSaltosLinea(datos):
        while (datos.find('\n') > 0):
            datos = datos.replace('\n', '')
        return datos