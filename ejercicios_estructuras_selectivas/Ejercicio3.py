#En la línea 1 se pregunta el monto total de la compra para saber si es mayor o menor a $500000
montoTotal=int(input("Digite el monto total de la compra:"))
#En las líneas del 4 hasta el 8 se hace el proceso y se aplican las condiciones del problema planteado dentro de la estructura IF cuando el valor supera los 500000, solicitando un préstamo al banco, cuánto pone de su capital y cuánto le solicita al fabricante
if montoTotal>500000:
    dineroPropio=montoTotal*0.55
    prestamoBanco=montoTotal*0.30
    creditoFabricante=(montoTotal*0.15)+(montoTotal*0.20)
    print("La empresa invirtió:",dineroPropio,"le solicitó prestado al banco:",prestamoBanco,"y el valor del crédito solicitado al fabricante fue de:",creditoFabricante)
#En las líneas de la 10 hasta la 13 se hace el mismo proceso que en la estructura IF pero con porcentajes distintos y sin solicitar el préstamo al banco, solo el capital y el préstamo al fabricante
else:
    dineroPropio=montoTotal*0.70
    creditoFabricante=(montoTotal*0.30)+(montoTotal*0.20)
    print("La empresa invirtió:",dineroPropio,"y el valor del crédito solicitado al fabricante fue de:",creditoFabricante)