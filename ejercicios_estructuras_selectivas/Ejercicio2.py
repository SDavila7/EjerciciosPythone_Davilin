#En las líneas 2 y 3 pregunta acerca del valor total de la compra de las zapatillas y la cantidad de zapatillas que compró
valorCompra=int(input("Digita el valor total de la compra de las zapatillas:"))
cantidadZapatillas=int(input("Digita la cantidad de pares de zapatillas que compraste: "))
#En las líneas 5 y 6 se utiliza la estructura if para saber si la cantidad de zapatillas que compró es mayor o igual a 3 para hacerle un descuento del 20%
if cantidadZapatillas>=3:
    descuento=0.20
#En las líneas 8 y 9 se utiliza la estructura else para saber si la cantidad de zapatillas que compró es menor a 3 para hacerle un descuento del 10%
else:
    descuento=0.10
#En las líneas 11 y 12 se aplica la operación de multiplicación y resta para sacar cuánto es el descuento que se le debe aplicar a la compra y el valor final a pagar
descuentoTotal=valorCompra*descuento
valorTotal=valorCompra-descuentoTotal
#Se muestra el valor final a pagar con el descuento incluido
print("El valor total de la compra es:",valorTotal)