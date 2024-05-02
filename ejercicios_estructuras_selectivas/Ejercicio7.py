#En la línea 2 se pregunta cuántas llantas compró para calcularle así mismo el precio
cantidadLlantas=int(input("Hola, puedes digitar cuántas llantas compraste por favor: "))
#En las líneas de la 4 hasta la 9 se utiliza la estructurta IF Y ELIF para saber de acuerdo a la cantidad de llantas cuánto cobrarle, si es menor a 5 se cobra 300, si la cantidad está entre 5 y 10 se cobra 250 pero si es mayor o igual a 11 se le cobra 200 (por cada llanta)
if cantidadLlantas<5:
    valorApagar=cantidadLlantas*300
elif cantidadLlantas>=5 and cantidadLlantas<=10:
    valorApagar=cantidadLlantas*250
elif cantidadLlantas>=11:
    valorApagar=cantidadLlantas*200
#En la línea 11 se imprime el resultado de cuánto debe pagar en total de acuerdo el precio por las llantas compradas
print("Deberás pagar: $",valorApagar, "en total por la cantidad de llantas que compraste.")