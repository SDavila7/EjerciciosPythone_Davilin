#Se llama e importa la estructura random en la línea 2 y 3
from random import *
import random
#En las líneas de la 5 hasta la 7 declaran los colores de las balotas y se utiliza la función random.choice para escoger un color al azar, luego se pregunta el valor de la compra (sin descuento)
coloresBalotas= ["verde", "rojo", "amarillo", "azul", "blanco", "negro", "rosado", "naranja"]
colorBalota = random.choice(coloresBalotas)
valorCompra=int(input("Digita el valor de la compra:"))
#En las líneas de la 8 hasta la 14 se utiliza la estructura IF-ELIF-ELSE para saber de acuerdo al color de la balota escogida cuál descuento aplicarle (20%,15% o 0%)
if colorBalota =="verde":
 descuento=valorCompra*0.20
elif colorBalota == "rojo":
 descuento=valorCompra*0.15
else:
 descuento=0
#En la línea 16 se hace la operación del valor de la compra menos el descuento y se guarda en la variable del valor total a pagar (con descuento)
valorTotal=valorCompra-descuento
#En la línea 17 imprime el valor de la compra, el color de la balota que se escogió, el descuento aplicado y el valor final a pagar
print("el valor de la compra es:",valorCompra,";El color de la balota es:",colorBalota,";El descuento:",descuento,"y el valor final a pagar es:",valorTotal)