nombreVendedor=(input("¿Cuál es tu nombre?"))#Se pregunta acerca del nombre del vendedor
sueldoBase=int(input("Digita tu sueldo:"))#Se pregunta sobre el sueldo que gana el vendedor sin nada de comisiones
comision=int(input("Digita el valor de la comisión:"))#Se pregunta sobre el valor que gana por cada comisión que realiza
numerosComision=int(input("Digita cuántas comisiones obtuviste:"))#Se pregunta cuántas comisiones obtuvo en el mes
comisionTotal=int #Se declara la variable "comisionTotal" cómo números enteros
comisionTotal=comision*numerosComision #Se realiza la operación de multiplicar el valor de la comisión que gana por el número de comisiones que hizo y se guarda en la variable "comisionTotal"
sueldoTotal=int #Se declara la variable "sueldoTotal" como números enteros
sueldoTotal=comisionTotal+sueldoBase #Se realiza la operación de sumar lo que hay en la varible "comisionTotal" más el sueldo base (lo que gana) y se guarda en la variable "sueldoTotal"
print("El trabajador", nombreVendedor,"tiene un sueldo de",sueldoBase,"durante el mes obtuvo una comisión de" ,comisionTotal,"y el valor final a pagar es:",sueldoTotal) #Se muestra el mensaje que dice el nombre del vendedor, el sueldo base, el valor de la comisión que gana y el valor final sumando las comisiones