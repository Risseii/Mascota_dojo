from ninja import Ninja
from mascota import Mascota
from subclase import subclase

#Primero se convoca la clase mascota que está dentro de Gato y se asocia con el primerninja

Gato = Mascota("Gato","mestizo","Croquetas")
Gato.sonido()
# Gato.printenergia(100)

print("---Deberes Ninja---")
primerninja = Ninja("ABC","DEF","2","Canbo",Gato)  
primerninja.caminar().alimentar().bañar()

print("---Gatito_Spock---")
Gatito = subclase("Spock","Mestizo","Croquetas","Juguetón","Blanco")
Gatito.info().sonido()

print("---Gataso_Garfield---")
Gataso = subclase("Garfield","Mestizo","Croquetas","Tranquilo","Naranja")
Gataso.info().sonido()

subclase.mostrar_lista_submascotas()