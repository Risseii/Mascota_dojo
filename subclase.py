from mascota import Mascota

class subclase(Mascota):
    
    lista_submascotas = []
    
    def __init__(self,name,tipo,golosinas,personalidad,color):
        super().__init__(name,tipo,golosinas)
        self.personalidad = personalidad
        self.color = color
        subclase.lista_submascotas.append(self)
    #sobre escribir
    def sonido(self):
        print("Miauuuuuu!!!!")
        return self
    
    def info(self):
        print(f"Mi nombre es {self.name},soy {self.tipo} de color {self.color} y muy {self.personalidad}")
        return self
    
    #Adicionales:
    def imprime(self):
        print(f"Nombre:{self.name},{self.color},{self.tipo}")
        return self
    
    @classmethod
    def mostrar_lista_submascotas(cls):
        print("Los gatos que tienes son: ")
        for cat in cls.lista_submascotas:
            cat.imprime()
