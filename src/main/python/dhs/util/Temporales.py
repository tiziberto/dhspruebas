class Temporales:
    
    
    def __init__(self):
        self.contador = 0
        
    def next_temporal(self):
        temporal = f't{self.contador}'
        self.contador += 1
        return temporal