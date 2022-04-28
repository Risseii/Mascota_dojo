class Ninja:
    
    def __init__(self,nombre,apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota= mascota
    
    def caminar(self):
        print(f"Sacar a {self.mascota.name} a pasear")
        self.mascota.jugar()
        return self
    
    def alimentar(self):
        print(f"Alimentar a {self.mascota.name} con {self.comida_mascota}")
        self.mascota.comer()
        return self
    
    def bañar(self):
        print(f"Bañar a {self.mascota.name}")
        self.mascota.sonido()
        return self
    


