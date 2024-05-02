#En la línea 2 se pregunta cuál es la cantidad de dinero que paga por la pensión
pension=int(input("Digita cuánto pagas de pensión: "))
#En la línea 4 se pregunta cuál fué el promedio del alumno el último periodo para ver si se aplica el descuento
promedio=float=(input("Digita el promedio que sacaste en este último periodo: "))
#En las líneas de la 6 hasta la 11 se utiliza la estructura IF y ELSE para saber el descuento o el precio total que debe pagar por la pensión este periodo dependiendo del promedio, si es mayor o igual a 9 se le hace el descuento, sino, no se le hace ningún descuento y se le cobra el IVA (10% de la pensión)
if promedio>="9":
    descuento=pension*0.30
    descuentoTotal=pension-descuento
else:
    descuento=pension*0.10
    descuentoTotal=pension+descuento
#En la línea 13 se imprime el resultado del valor total a pagar con o sin el descuento dependiendo del proceso anterior
print("El alumno deberá pagar: $",descuentoTotal,"este periodo.") 