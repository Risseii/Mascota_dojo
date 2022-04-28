class Mascota:
    
    def __init__(self,name,tipo,golosinas):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 0
        self.energia = 0
    
    def dormir(self):
        self.energia += 25
        return self
        
    def comer(self):
        self.energia += 5
        self.salud += 10
        return self
    
    def jugar(self):
        self.salud += 5
        return self
    
    def sonido(self):
        print("Sonido del animal")

    # def printenergia(self,amount):
    #     self.energia += amount
    #     print(f"La energía total de tu mascota es {self.energia}")
    #     return self
    